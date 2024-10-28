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
