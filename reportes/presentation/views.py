# views.py
from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from reportes.application.use_cases.generar_factura import GenerarFactura
from reportes.infraestructure.mappers.reports import BillReportUtil
from .serializers import BillSerializer


class GenerarFacturaView(APIView):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.report = GenerarFactura(BillReportUtil())

    def post(self, request: Request):
        try:
            archivo_excel = request.FILES["report"]

            if archivo_excel is None:
                return Response(
                    {
                        "error": "No se ha proporcionado ningun archivo para obtener las facturacion."
                    },
                    status=400,
                )

            res = self.report.ejecutar(archivo_excel)
            serializer = BillSerializer(res, many=True)
            return Response({"facturas": serializer.data})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
