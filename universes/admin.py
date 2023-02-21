from django.contrib import admin

from .models import Universe


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
