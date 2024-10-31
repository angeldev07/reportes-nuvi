# urls.py
from django.urls import path
from .views import GenerarFacturaView

urlpatterns = [
    path("generar-factura", GenerarFacturaView.as_view(), name="generar_factura"),
]
