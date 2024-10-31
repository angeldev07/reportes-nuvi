from typing import Dict, List
from datetime import datetime
from .House import CondominioHouse


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

