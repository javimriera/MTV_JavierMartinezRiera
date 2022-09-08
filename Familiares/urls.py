from django.contrib import admin
from django.urls import path
from Familiares.views import listar_familiares

urlpatterns = [
    path('', listar_familiares),
]
