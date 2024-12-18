from django.urls import path
from .views import addVehiculoView, listarVehiculosView
urlpatterns = [
    path('add', addVehiculoView, name='vehiculoIndex'),
    path('listar',listarVehiculosView.as_view(), name="listarVehiculos")
]