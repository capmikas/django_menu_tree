from django.http import HttpResponse
from django.shortcuts import render
from app_tree_menu.models import MenuItem


def index(request):
    return render(request, 'app_tree_menu/index.html')

# def switch_to_menu_item(request, item_slug):
#     return HttpResponse(f"Переход на пункт меню со слагом: {item_slug}")

def switch_to_menu_item(request, item_slug):
    # content = {'text': item_slug}
    item = MenuItem.objects.get(slug=item_slug)
    content = {'item': item}
    return render(request, 'app_tree_menu/menu_item.html', context=content)


