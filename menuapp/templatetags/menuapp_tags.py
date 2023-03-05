from django.urls import reverse
from django import template
from menuapp.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    return render_menu(request, menu_items)

def render_menu(request, menu_items):
    current_path = request.path
    menu_html = '<ul>'
    for item in menu_items:
        active_class = ''
        if item.url and current_path.startswith(item.url):
            active_class = 'active'
        elif item.named_url and current_path.startswith(reverse(item.named_url, args=(item.pk,))):
            active_class = 'active'
        menu_html += f'<li class="{active_class}"><a href="{item.url or reverse(item.named_url, args=[item.pk])}">{item.title}</a>'
        if item.children.exists():
            menu_html += render_menu(request, item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
