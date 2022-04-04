from django.contrib import admin
from . models import Entities


class EntitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Entities, EntitiesAdmin)
