from django.urls import path, include

urlpatterns = [
    path("reportes/", include("reportes.presentation.urls")),
]
