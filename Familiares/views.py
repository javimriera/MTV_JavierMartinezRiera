from django.template import Template, Context, loader
from Familiares.models import Familia
from django.http import HttpResponse

def probandotemplate(self):
    mihtml= open("familiares_list.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento= plantilla.render(micontexto)

    return HttpResponse(documento)
