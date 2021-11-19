from django.contrib import admin

from apps.docente.models import Docente, antecedentes_medico

# Register your models here.

admin.site.register(Docente)
admin.site.register(antecedentes_medico)