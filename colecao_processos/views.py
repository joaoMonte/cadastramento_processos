from django.http import JsonResponse


# Create your views here.
def processos(request):
    data = {"oi": "2"}
    return JsonResponse(data)