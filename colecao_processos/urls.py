from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaProcessos, name='lista processos'),
]