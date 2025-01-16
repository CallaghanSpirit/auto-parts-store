from django.shortcuts import render,HttpResponse,get_object_or_404
from goods.models import Goods, Category

# Create your views here.
def index(request):
    goods = Goods.manager.all()
    data = {
        'title':'Главная страница',
        'goods':goods
        
        }
    return render(request,template_name='goods/index.html',context=data)

def category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    goods = Goods.manager.filter(cats_id=category.pk)
    data = {'title':'Категории',
            'goods':goods,}
    return render(request,template_name='goods/category.html',context=data)

def cardpage(request,gd_slug):
    goods = get_object_or_404(Goods,slug=gd_slug)
    data = {"goods":goods,}
    return render(request,template_name='goods/cardpage.html',context=data)

