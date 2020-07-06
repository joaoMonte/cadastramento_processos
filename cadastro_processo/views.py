import csv
from django.shortcuts import render
from django.apps import apps
from .forms import UploadPlanilha
from .models import Planilha

# Create your views here.
def upload(request):
    form = UploadPlanilha()
    if request.method == 'POST':
        form = UploadPlanilha(request.POST, request.FILES)
        if form.is_valid():
            nome = request.POST['nome']
            cliente = request.POST['cliente']
            arquivo = request.FILES['planilha']
            novaPlanilha = Planilha(nome=nome, cliente=cliente, arquivo=arquivo)
            novaPlanilha.save()
            #Chama a função para processamento dos CSVs 
            processaCsv(arquivo)
    return render(request, 'uploadScreen.html', locals())

def processaCsv(filename):
    #Processa o csv e cria modelos do tipo Processo com as informações contidas
    #na planilha
    csvfile = filename.read().decode("utf-8") 
    #Carrega dinamicamente o modelo Processo
    Processo = apps.get_model('colecao_processos', 'Processo')
    for line in csvfile.split('\n'):
        if line:
            pasta, comarca, uf = line.split(';') 
            uf = uf.replace("\r", "")
            novoProcesso = Processo(pasta=pasta, comarca=comarca, uf=uf)
            novoProcesso.save()
    
