from django.contrib import admin
from django.urls import path, include
from .views import indexView, registroView, loginView, logoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index'),
    path('signup/', registroView, name="signup"),
    path('signin/', loginView, name='signin'),
    path('signout/', logoutView, name='signout'),
    path('vehiculo/', include('vehiculo.urls')),
]
