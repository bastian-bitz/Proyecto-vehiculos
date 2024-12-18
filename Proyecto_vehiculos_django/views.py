from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from vehiculo.models import Vehiculo
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def registroView(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permiso = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
            user = form.save()
            user.user_permissions.add(permiso)
            login(request, user)
            messages.success(request, "Registrado satisfactoriamente")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
    else:
        form = RegistroUsuarioForm()

    return render(request, "signup.html", {"register_form":form})

def loginView(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"iniciaste sesión como: {username}")
            return redirect('index')
        else:
            messages.error(request, "Invalido username o password.")
    context = {}
    return render(request, 'signin.html', context)

def logoutView(request):
    logout(request)
    return redirect('signin')

