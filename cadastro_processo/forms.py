from django import forms

class UploadPlanilha(forms.Form):
    #Form para permitir a criação de instancias do modelo Planilha
    nome = forms.CharField(max_length=50)
    cliente = forms.CharField(max_length=50)
    planilha = forms.FileField()
    