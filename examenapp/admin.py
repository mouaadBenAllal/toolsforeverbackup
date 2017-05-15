from django.contrib import admin
from .models import Fabriek
# Register your models here.


class FabriekAdmin(admin.ModelAdmin):
    model = Fabriek
    list_display = ('id', 'fabrieksnaam', 'telefoonnummer',)

admin.site.register(Fabriek, FabriekAdmin)
