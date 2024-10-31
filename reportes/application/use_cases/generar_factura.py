from reportes.infraestructure.mappers.reports import BillReportUtil, HouseReport


class FileNotSupported(Exception):
    def __init__(
        self, message="La extension del archivo no esta soportada en esta version."
    ):
        self.message = message

        super().__init__(self.message)


class GenerarFactura:
    def __init__(self, excel_mapper: BillReportUtil):
        self.excel_mapper = excel_mapper
        self.content_type = (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    def ejecutar(self, archivo_excel):

        if archivo_excel.content_type != self.content_type:
            raise FileNotSupported()

        self.excel_mapper.read_excel(archivo_excel)
        facturas = self.excel_mapper.generatereport()
        return facturas
