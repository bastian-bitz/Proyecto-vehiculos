from django.shortcuts import render
from .forms import VehiculoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from .models import Vehiculo
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
# Create your views here.

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def addVehiculoView(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehículo creado satisfactoriamente")
    else:
        form = VehiculoForm()
    return render(request, 'add_vehiculo.html', {'form': form})

class listarVehiculosView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Vehiculo
    template_name = "listar_vehiculo.html"
    context_object_name ='vehiculos'
    permission_required = 'vehiculo.visualizar_catalogo'
