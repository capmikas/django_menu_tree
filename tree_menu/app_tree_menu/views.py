from django.shortcuts import render


def draw_menu(request, item_slug=''):
    return render(request, 'app_tree_menu/index.html')
