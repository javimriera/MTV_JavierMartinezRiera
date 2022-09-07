from django.shortcuts import render
from django.template import Template, Context, loader
from Familiares.models import Familia
from django.http import HttpResponse


def listar_familiares(request):
    queryset= Familia.objects.all()
    diccionario= {'Familiares': queryset}
    plantilla= loader.get_template('familiares_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)
    
def probar_template(request):
    with open('C:\Users\javim\Documents\Javi\Coderhouse\Python\1erEntregableCoder\MTV_JavierMartinezRiera\MTV_JMR\Familiares\templates\Familiares\familiares_list.html') as archivo:
        plantilla = Template(archivo.read())
    contexto = Context()
    documento_html= plantilla.render(contexto)
    
    return HttpResponse(documento_html)