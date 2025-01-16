from django import template
import goods.views as views
from goods.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats

@register.inclusion_tag('goods/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats':cats}