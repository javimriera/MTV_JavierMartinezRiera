from django.template import Template, Context, loader
from Familiares.models import Familia
from django.http import HttpResponse


def listar_familiares(request):
    queryset = Familia.objects.all()
    diccionario = {'Familiares': queryset}
    plantilla= loader.get_template('familiares_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)
    