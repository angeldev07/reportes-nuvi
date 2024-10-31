from typing import Dict, List
from pandas import DataFrame
import pandas as pd


class CondominioHouse:
    def __init__(self, id: str, nombre_cliente: str, propiedad: str):
        self.id: str = id
        self.nombre_cliente: str = nombre_cliente
        self.propiedad: str = propiedad

    def __str__(self):
        return (
            f"CondominioHouse(id='{self.id}', nombre_cliente='{self.nombre_cliente}', "
            f"propiedad='{self.propiedad}')"
        )

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre_cliente": self.nombre_cliente,
            "propiedad": self.propiedad,
        }


class House:

    def __init__(
        self,
        bloque: str,
        nomenclatura: str,
        cliente: CondominioHouse,
        piso: str = None,
        tipo_propiedad: str = "CASA",
    ):
        self.bloque: str = bloque
        self.nomenclatura: str = nomenclatura
        self.cliente: CondominioHouse = cliente
        self.piso: str = piso
        self.tipo_propiedad: str = tipo_propiedad

    def __str__(self):
        return (
            f"House(bloque='{self.bloque}', nomenclatura='{self.nomenclatura}', "
            f"cliente={self.cliente}, piso='{self.piso}', "
            f"tipo_propiedad='{self.tipo_propiedad}')"
        )

    def to_dict(self) -> Dict:
        return {
            "bloque": self.bloque,
            "nomenclatura": self.nomenclatura,
            "cliente": self.cliente.to_dict(),
            "piso": self.piso,
            "tipo_propiedad": self.tipo_propiedad,
        }

    def to_nuvi(self) -> Dict:
        return {
            "propiedad": {
                "tipo_propiedad": self.tipo_propiedad,
                "bloque": self.bloque,
                "piso": self.piso,
                "nomenclatura": self.nomenclatura,
            },
            "cliente": {
                "id": self.cliente.id,
                "cedula": None,
                "nombre": self.cliente.nombre_cliente,
                "propiedad": self.cliente.propiedad,
            },
        }
