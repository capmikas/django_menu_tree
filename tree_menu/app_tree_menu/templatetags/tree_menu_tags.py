from django import template
from app_tree_menu.models import MenuItem
from collections import defaultdict

register = template.Library()

@register.inclusion_tag('app_tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = str(context.get('request'))
    current_slug = request[request.find("'")+1 : request.rfind("'")]
    current_slug = current_slug[current_slug.rfind('/', 0, -1) + 1: -1] if not current_slug == '/' else None
    menu_items = MenuItem.objects.all().filter(menu_type__name=menu_name).order_by('name')
    children = defaultdict(list)
    current_item = None
    for item in menu_items:
        parent_id = item.parent.id if item.parent else None
        children[parent_id].append(item)
        if item.slug == current_slug:
            current_item = item
    result_menu_list = []
    parents_list = []

    def find_parent(item):
        parents_list.append(item)
        if item.parent:
            find_parent(item.parent)

    if current_item:
        find_parent(current_item)

    def create_menu_list(parent_id, level):
        for child in children.get(parent_id, []):
            result_menu_list.append((child, level))
            if child in parents_list:
                create_menu_list(child.id, level + 1)

    create_menu_list(None, 0)
    return {'menu': result_menu_list, 'menu_name' : menu_name, 'current_item' : current_item}


@register.filter
def indent(level):
    return '-' * (level * 2)