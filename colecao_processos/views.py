from django.http import JsonResponse
from colecao_processos.models import Processo

# Create your views here.
def listaProcessos(request):
    output_json = {"Processos": []}
    for processo in Processo.objects.all():
        processo_json = {
            "pasta": processo.pasta,
            "comarca": processo.comarca,
            "uf": processo.uf
        }
        output_json["Processos"].append(processo_json)
    return JsonResponse(output_json)