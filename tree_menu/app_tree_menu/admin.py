from django.contrib import admin
from .models import MenuItem, MenuType


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug', 'menu_type')
    list_display_links = ('id', 'name', 'slug')
    ordering = ['name', 'parent']

admin.site.register(MenuItem, MenuItemAdmin)

class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['name']

admin.site.register(MenuType, MenuTypeAdmin)