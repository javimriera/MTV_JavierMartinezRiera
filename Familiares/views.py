from django.shortcuts import render
from django.template import Template, Context, loader
from Familiares.models import Familia
from django.http import HttpResponse


def listar_familiares(request):
    familiares= Familia.objects.all()
    return render(request, "familiares_list.html",{"familiares":familiares})
  
  
   #    queryset= Familia.objects.all()
   # diccionario= {'Familiares': queryset}
    #plantilla= loader.get_template('familiares_list.html')
    #documento_html = plantilla.render(diccionario)

    #return HttpResponse(documento_html)