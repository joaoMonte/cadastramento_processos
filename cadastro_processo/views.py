import csv
from django.shortcuts import render
from .forms import UploadPlanilha
from .models import Planilha
#from cadastramento_processos.colecao_processos.models import Processo

# Create your views here.

def upload(request):
    form = UploadPlanilha()
    if request.method == 'POST':
        form = UploadPlanilha(request.POST, request.FILES)  # Do not forget to add: request.FILES
        if form.is_valid():
            print(request.FILES)
            print(request.FILES['planilha'])
            #Criar modelo 
            # Do something with our files or simply save them
            # if saved, our files would be located in media/ folder under the project's base folder
            #form.save()
    return render(request, 'uploadScreen.html', locals())



