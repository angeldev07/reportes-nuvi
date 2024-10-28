from datetime import datetime
from typing import List, Dict, Tuple
from pandas import DataFrame
import pandas as pd
from house_report import CondominioHouse, HouseReport


class BillConcepts:
    def __init__(self, descripcion: str, valorTotal: float):
        self.descripcion = descripcion
        self.valorTotal = valorTotal

    def __str__(self):
        return (
            f'{{"descripcion": "{self.descripcion}", "valorTotal": {self.valorTotal}}}'
        )

    def to_dict(self) -> Dict:
        return {"descripcion": self.descripcion, "valorTotal": self.valorTotal}


class BillPayInfo:
    def __init__(self, total: float, fecha: datetime):
        self.total = total
        self.fecha = fecha

    def to_dict(self) -> Dict:
        return {
            "total": self.total,
            "fecha": self.fecha.isoformat(),
        }


class Bill:

    def __init__(
        self,
        periodo: str,
        prontoPago: BillPayInfo,
        despuesPago: BillPayInfo,
        conceptos: List[BillConcepts],
        propietario: CondominioHouse,
    ):
        self.periodo = periodo
        self.prontoPago = prontoPago
        self.despuesPago = despuesPago
        self.conceptos = conceptos
        self.propietario = propietario

    def __str__(self):
        conceptos_str = [str(concepto) for concepto in self.conceptos]
        return f'{{"periodo": "{self.periodo}", "fecha": "{self.fecha}", "total": {self.total}, "conceptos": {conceptos_str}}}'

    def to_dict(self) -> Dict:
        return {
            "periodo": self.periodo,
            "prontoPago": self.prontoPago.to_dict(),
            "despuesPago": self.despuesPago.to_dict(),
            "conceptos": [concepto.to_dict() for concepto in self.conceptos],
            "cliente": self.propietario.to_dict(),
        }


class BillReportUtil:

    def __init__(self, path):
        self.excel_value: DataFrame = None

        if not path is None:
            self.read_excel(path)

    def read_excel(self, path):
        self.excel_value = pd.read_excel(path, sheet_name="base".upper())

    def getperiod(self) -> Tuple[str, int]:
        months_mapping = {
            "enero": 1,
            "febrero": 2,
            "marzo": 3,
            "abril": 4,
            "mayo": 5,
            "junio": 6,
            "julio": 7,
            "agosto": 8,
            "septiembre": 9,
            "octubre": 10,
            "noviembre": 11,
            "diciembre": 12,
        }
        month = self.excel_value.columns[0].split(" ")[0].lower()
        return (month, months_mapping[month])

    def resetvalues(self):
        self.excel_value = self.excel_value.iloc[0:].reset_index(
            drop=True
        )  # Elimina la primera fila y reinicia el índice
        self.excel_value.columns = self.excel_value.iloc[
            0
        ]  # Usa la primera fila como encabezado
        self.excel_value = self.excel_value.iloc[0:].reset_index(
            drop=True
        )  # Elimina la fila que ahora es el encabezado y reinicia el índice

    def getpaydates(
        self, headers: List[str], periodo: int
    ) -> Tuple[datetime, datetime]:
        firstdate, seconddate = headers[0].split(" "), headers[1].split(" ")
        firstdate, seconddate = max(
            [int(day) for day in firstdate if day.isdigit() and len(day) <= 2]
        ), max([int(day) for day in seconddate if day.isdigit() and len(day) <= 2])
        return (
            (
                datetime(datetime.now().year, periodo - 1, firstdate),  # pronto pago
                datetime(datetime.now().year, periodo - 1, seconddate),  # despues pago
            )
            if firstdate < seconddate
            else (
                datetime(datetime.now().year, periodo, seconddate),  # pronto pago
                datetime(datetime.now().year, periodo, firstdate),  # despues pago
            )
        )

    def generatereport(self) -> List[Bill]:
        period = self.getperiod()  # extraer el periodo de facturacion.
        self.resetvalues()  # resetear los valores, se hace para borrar la primera fila del reporte que corresponde al mes reportado.

        concepts = self.excel_value.iloc[
            3:-3, 4:10
        ]  # se obtiene un subconjunto del dateframe que corresponden a los conceptos de la factura.
        totalPays = self.excel_value.iloc[
            3:-3, 10:12
        ]  # se obtiene un subconjunto del dateframe que corresponde a los totales a pagar, pronto y despues pago
        houses = self.excel_value.iloc[
            3:-3, 2:4
        ]  # se obtiene un subconjuto del datafrem que corresponde a las casas/lotes
        dates = self.getpaydates(
            totalPays.columns.to_list(), period[1]
        )  # se obtiene las fechas de pronto pago y despues.

        report: List[Bill] = []

        for (_, concept_row), (_, pay_row), (_, house_row) in zip(
            concepts.iterrows(), totalPays.iterrows(), houses.iterrows()
        ):
            billconcepts: List[BillConcepts] = []
            for descripcion, valor in concept_row.items():
                if pd.notna(valor):
                    valor_float = float(valor) if pd.notna(valor) else 0
                    billconcepts.append(BillConcepts(descripcion, valor_float))

            despues_pago = float(pay_row.iloc[0]) if pd.notna(pay_row.iloc[0]) else 0
            pronto_pago = (
                float(pay_row.iloc[1])
                if len(pay_row) > 1 and pd.notna(pay_row.iloc[1])
                else 0
            )
            lote, housesInfo = house_row.get("CASA/LT"), house_row.get(
                "NOMBRES Y APELLIDOS"
            )

            report.append(
                Bill(
                    periodo=period[1],
                    conceptos=billconcepts,
                    prontoPago=BillPayInfo(pronto_pago, dates[0]),
                    despuesPago=BillPayInfo(despues_pago, dates[1]),
                    propietario=HouseReport.buildhouseobjE(
                        housesInfo.split("-"), lote
                    ).cliente,
                )
            )

        return report
