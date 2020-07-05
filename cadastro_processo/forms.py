from django import forms


class UploadPlanilha(forms.Form):
    #nome = models.CharField(max_length=50)
    #cliente = models.CharField(max_length=50)
    planilha = forms.FileField()
    