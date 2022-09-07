from django.urls import path
from Familiares.views import listar_familiares, probar_template

urlpatterns = [
    path('', listar_familiares),
    path('', probar_template),
]
