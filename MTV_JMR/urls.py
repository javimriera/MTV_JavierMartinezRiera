from django.contrib import admin
from django.urls import path, include

from Familiares.views import probandotemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('probandoTemplate/', probandotemplate)
]
