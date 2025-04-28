from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from app_tree_menu.models import MenuItem


def index(request):
    return render(request, 'app_tree_menu/index.html')


def switch_to_menu_item(request, item_slug):
    item = get_object_or_404(MenuItem, slug=item_slug)
    content = {'item': item}
    return render(request, 'app_tree_menu/menu_item.html', context=content)


