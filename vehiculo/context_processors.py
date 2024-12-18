# vehiculo/context_processors.py

def add_vehicle_permission(request):
    return {
        'can_add_vehicle': request.user.has_perm('vehiculo.add_vehiculo')
    }
