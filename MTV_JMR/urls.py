from django.contrib import admin
from django.urls import path, include

from Familiares.views import listar_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Familiares/', listar_familiares)
]
