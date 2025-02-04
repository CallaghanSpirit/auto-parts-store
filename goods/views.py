from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from goods.models import Goods, Category, Tags
from goods.forms import AddPostForm, UploadFileForm
from pathlib import Path
from django.core.exceptions import ValidationError


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
    return render(request,template_name='goods/index.html',context=data)

def cardpage(request,gd_slug):
    goods = get_object_or_404(Goods,slug=gd_slug)
    data = {"goods":goods,}
    return render(request,template_name='goods/cardpage.html',context=data)

def show_tag(request, tag_slug):
    tag = get_object_or_404(Tags, slug=tag_slug)
    goods = tag.gtags.filter(status=Goods.Status.IN_STOCK)

    data = {
        'title':f"Тег: {tag}",
        'goods':goods,
    }
    return render(request, 'goods/index.html', context=data)

def add_prod(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # try:
            #     Goods.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, "Ошибка добавления товара")
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    
    data = {
        'title':'Добавление товара',
        'form':form   

            }
    return render(request, 'goods/add_prod.html', context=data)

def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
        # handle_uploaded_file(request.FILES['file_upload'])
    else:
        form = UploadFileForm()
    data = {
        'title': 'О сайте',
        'form': form,


    }
    return render(request, 'goods/about.html', context=data)

