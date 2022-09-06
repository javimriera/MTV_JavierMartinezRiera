# MTV_JavierMartinezRiera
def listar_familiares(request):
    queryset = Familia.objects.all()
    diccionario = {'Familiares': queryset}
    plantilla= loader.get_template('familiares_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)