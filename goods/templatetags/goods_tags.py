from django import template
import goods.views as views
from goods.models import Category, Tags

register = template.Library()

@register.inclusion_tag('goods/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats':cats}

@register.inclusion_tag('goods/list_tags.html')
def show_tags():
    return {'tags': Tags.objects.all() }