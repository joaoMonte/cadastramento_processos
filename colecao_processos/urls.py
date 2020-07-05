from django.urls import path
from . import views

urlpatterns = [
    path('', views.processos, name='lista_processos'),
]