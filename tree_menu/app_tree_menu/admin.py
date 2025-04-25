from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug')
    list_display_links = ('id', 'name', 'slug')
    ordering = ['name', 'parent']

admin.site.register(MenuItem, MenuItemAdmin)
