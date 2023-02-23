from django.contrib import admin

from .models import Universe, Post


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'universe')
