from django.shortcuts import render,HttpResponse,get_object_or_404

# Create your views here.
def index(request):
    data = {'title':'Главная страница'}
    return render(request,template_name='goods/index.html',context=data)

def category(request):
    data = {'title':'Категории'}
    return render(request,template_name='goods/category.html',context=data)

def cardpage(request):
    goods= get_object_or_404()
    return render(request,template_name='goods/cardpage.html')

cats = [{'id':1,'name':'Кексы'},
        {'id':2, 'name':'Блины'},
        {'id':3, 'name':'Торты'}]