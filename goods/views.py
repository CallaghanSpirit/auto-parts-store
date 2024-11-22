from django.shortcuts import render,HttpResponse,get_object_or_404
from goods.models import Goods

# Create your views here.
def index(request):
    goods = Goods.objects.all()
    data = {
        'title':'Главная страница',
        'goods':goods
        
        }
    return render(request,template_name='goods/index.html',context=data)

def category(request):
    data = {'title':'Категории'}
    return render(request,template_name='goods/category.html',context=data)

def cardpage(request,gd_slug):
    goods = get_object_or_404(Goods,slug=gd_slug)
    data = {"goods":goods}
    return render(request,template_name='goods/cardpage.html',context=data)

cats = [{'id':1,'name':'Кексы'},
        {'id':2, 'name':'Блины'},
        {'id':3, 'name':'Торты'}]