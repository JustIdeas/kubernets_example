from django.contrib import admin
from game.models import store

class Game(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    list_display_links = ('name', 'category')
    search_fields = ('name', 'category',)
admin.site.register(store, Game)       