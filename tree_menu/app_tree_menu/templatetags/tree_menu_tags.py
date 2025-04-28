from django import template
from app_tree_menu.models import MenuItem
from collections import defaultdict

register = template.Library()

@register.inclusion_tag('app_tree_menu/menu.html')
def draw_menu(menu_name, item1=0):
    menu_items = MenuItem.objects.all().filter(menu_type__name=menu_name).order_by('name')
    children = defaultdict(list)
    # Строим словарь детей для каждого родителя
    for item in menu_items:
        parent_id = item.parent.id if item.parent else None
        children[parent_id].append(item)
    result = []
    # Рекурсивная функция для обхода дерева
    def traverse(parent_id, level):
        # Сортируем детей текущего родителя по имени
        for child in sorted(children.get(parent_id, []), key=lambda x: x.name):
            result.append((child, level))
            traverse(child.id, level + 1)
    # Начинаем обход с корневых элементов (parent_id=None)
    traverse(None, 0)
    if item1:
        print('item', item1.slug)
    else:
        print('0000')
    return {'menu': result, 'menu_name' : menu_name}


@register.filter
def indent(level):
    return '-' * (level * 2)