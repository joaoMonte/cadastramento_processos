from django.urls import path
from . import views

urlpatterns = [
    path('', views.processos, name='raiz_processos'),
]