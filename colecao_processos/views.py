from django.http import JsonResponse
from django.apps import apps
from colecao_processos.models import Processo

# Create your views here.
def listaProcessos(request):
    models = apps.get_app_config('colecao_processos').get_models()
    output_json = {"Processos": []}
    for processo in Processo.objects.all():
        processo_json = {
            "pasta": processo.pasta,
            "comarca": processo.comarca,
            "uf": processo.uf
        }
        output_json["Processos"].append(processo_json)
    return JsonResponse(output_json)