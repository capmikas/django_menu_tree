from django.http import HttpResponse
from django.shortcuts import render
from app_tree_menu.models import MenuItem


def index(request):
    content = {'menu' : MenuItem.objects.all()}
    return render(request, 'app_tree_menu/index.html', context=content)

def switch_to_menu_item(request, item_slug):
    return HttpResponse(f"Переход на пункт меню со слагом: {item_slug}")
