from django import template
import goods.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats

@register.inclusion_tag('goods/list_categories.html')
def show_categories():
    cats = views.cats
    return {'cats':cats}