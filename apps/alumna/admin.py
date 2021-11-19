from django.contrib import admin

from apps.alumna.models import antecedentes_medico, Alumna

# Register your models here.

class AlumnaAdmin(admin.ModelAdmin):
    #list_display = ('id','codigo', 'nombres', 'edad')
    #fields = ('codigo','nombres','edad')
    search_fields = ["nombres"]

admin.site.register(antecedentes_medico)
admin.site.register(Alumna)
#admin.site.register(AlumnaAdmin)

