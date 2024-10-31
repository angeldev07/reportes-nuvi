from typing import Dict, List, Tuple
from pandas import DataFrame
from datetime import datetime
from reportes.domain.Bill import Bill, BillConcepts, BillPayInfo
from reportes.domain.House import House, CondominioHouse
import pandas as pd


class HouseReport:

    def __init__(self, path):
        self.excel_value: DataFrame = None

        if not path is None:
            self.read_excel(path)

    def read_excel(self, path):
        self.excel_value = pd.read_excel(
            path, sheet_name="base".upper(), skiprows=1, header=0
        )

    def buildhouseobj(self, houseInfo, lote) -> House:
        house, owner = houseInfo[0], houseInfo[1]
        bloque, nomenclatura = house[0], house[1:]

        return House(
            bloque=bloque,
            nomenclatura=nomenclatura,
            cliente=CondominioHouse(id=lote, nombre_cliente=owner, propiedad=house),
        )

    @staticmethod
    def buildhouseobjE(houseInfo, lote) -> House:
        house, owner = houseInfo[0], houseInfo[1]
        bloque, nomenclatura = house[0], house[1:]

        return House(
            bloque=bloque,
            nomenclatura=nomenclatura,
            cliente=CondominioHouse(id=lote, nombre_cliente=owner, propiedad=house),
        )

    def gethousesreport(self):
        houseInfo = self.excel_value.iloc[2:-3, 2:4]
        houses: List[House] = []

        for index, value in houseInfo.iterrows():
            lote, housesInfo = value.get("CASA/LT"), value.get("NOMBRES Y APELLIDOS")
            houses.append(self.buildhouseobj(housesInfo.split("-"), lote))

        return houses


class BillReportUtil:

    HOUSES_COLS = {
        "NUMERAL": "N",
        "HOUSE_NUMBER": "CASA/LT",
        "OWNER": "NOMBRES Y APELLIDOS",
    }

    CONCEPTS_COLS = {"CONCEPTS": "CONCEPTOS", "EARLY_PAY": "PRONTO PAGO"}

    def __init__(self, file=None):
        self.excel_value: DataFrame = None
        self.excel_cp: datetime = None

        if not file is None:
            self.read_excel(file)

    def read_excel(self, file):
        self.excel_value = pd.read_excel(file, sheet_name="Facturas")

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
        self.excel_value.iloc

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

    def getIndexConcepts(self, col_tuple):
        i, col = col_tuple
        if isinstance(col, str) and col.strip().upper() in list(self.CONCEPTS_COLS.values()):
            return i
        return None

    def generatereport(self) -> List[Bill]:

        houses = self.excel_value[list(self.HOUSES_COLS.values())].drop([0])

        concetpsindex = [
            index
            for index in map(self.getIndexConcepts, enumerate(self.excel_value.columns))
            if index is not None
        ]

        concepts = self.excel_value.iloc[:, concetpsindex[0] : concetpsindex[1]]
        conceptsnames = concepts.loc[0].values
        concepts =  concepts.drop([0])
        
        # concepts response 
        report: List[Bill] = []


        for  (conceptname), (_, concept_row), (_, house_row) in zip(
            conceptsnames, concepts.iterrows(), houses.iterrows()
        ):
            print('concepto:',conceptname)
            print('conceptos', concept_row.values)
            print('casa', house_row.values)
            print("p----------------------------------------------------p")
            pass
            # billconcepts: List[BillConcepts] = []
            # for descripcion, valor in concept_row.items():
            #     if pd.notna(valor):
            #         valor_float = float(valor) if pd.notna(valor) else 0
            #         billconcepts.append(BillConcepts(descripcion, valor_float))

            # despues_pago = float(pay_row.iloc[0]) if pd.notna(pay_row.iloc[0]) else 0
            # pronto_pago = (
            #     float(pay_row.iloc[1])
            #     if len(pay_row) > 1 and pd.notna(pay_row.iloc[1])
            #     else 0
            # )
            # lote, housesInfo = house_row.get("CASA/LT"), house_row.get(
            #     "NOMBRES Y APELLIDOS"
            # )

            # report.append(
            #     Bill(
            #         periodo=period[1],
            #         conceptos=billconcepts,
            #         prontoPago=BillPayInfo(pronto_pago, dates[0]),
            #         despuesPago=BillPayInfo(despues_pago, dates[1]),
            #         propietario=HouseReport.buildhouseobjE(
            #             housesInfo.split("-"), lote
            #         ).cliente,
            #     )
            # )

        return report
