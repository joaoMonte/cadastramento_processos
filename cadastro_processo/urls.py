from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaPlanilhas, name='lista planilhas'),
    path('/upload', views.upload, name='upload de planilha'),
]