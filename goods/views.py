from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from goods.models import Goods, Category, Tags, UploadFiles
from goods.forms import AddPostForm, UploadFileForm
from pathlib import Path
from django.core.exceptions import ValidationError
from django.views import View
from django.views.generic import  ListView, DetailView, FormView
from django.urls import reverse_lazy


# Create your views here.
# def index(request):
#     goods = Goods.manager.all()
#     data = {
#         'title':'Главная страница',
#         'goods':goods
        
#         }
#     return render(request,template_name='goods/index.html',context=data)

class GoodsHome(ListView):
    # model = Goods
    template_name = "goods/index.html"
    context_object_name = 'goods'
    extra_context = {
        'title':'Главная страница',
        
        }
    def get_queryset(self):
        return Goods.manager.all()
    
    # Работает при непосредственном вызове Get запроса
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Пидор'
   

# def category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     goods = Goods.manager.filter(cats_id=category.pk)
#     data = {'title':'Категории',
#             'goods':goods,}
#     return render(request,template_name='goods/index.html',context=data)

class GoodsCategory(ListView):
    # model = Category
    template_name = "goods/index.html"
    context_object_name = "goods"
    allow_empty = True
    
    def get_queryset(self):
        return Goods.manager.filter(cats__slug=self.kwargs['cat_slug'])

def cardpage(request,gd_slug):
    goods = get_object_or_404(Goods,slug=gd_slug)
    data = {"goods":goods,}
    return render(request,template_name='goods/cardpage.html',context=data)

class CardPage(DetailView):
    # model = Goods
    template_name = 'goods/cardpage.html'
    slug_url_kwarg = 'gd_slug'
    context_object_name = 'goods'

    def get_object(self, queryset = ...):
        return get_object_or_404(Goods.manager, slug = self.kwargs[self.slug_url_kwarg])

# def show_tag(request, tag_slug):
#     tag = get_object_or_404(Tags, slug=tag_slug)
#     goods = tag.gtags.filter(status=Goods.Status.IN_STOCK)

#     data = {
#         'title':f"Тег: {tag}",
#         'goods':goods,
#     }
#     return render(request, 'goods/index.html', context=data)

class GoodsTags(ListView):
    template_name = 'goods/index.html'
    context_object_name = 'goods'
    def get_queryset(self):
        return Goods.manager.filter(tags__slug=self.kwargs['tag_slug'])


# def add_prod(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
    
#     data = {
#         'title':'Добавление товара',
#         'form':form   

#             }
#     return render(request, 'goods/add_prod.html', context=data)


class AddProd(FormView):
    form_class = AddPostForm
    template_name = 'goods/add_prod.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class AddProd(View):
#     def get(self, request):
#         form = AddPostForm()
#         data = {
#         'title':'Добавление товара',
#         'form':form   

#             }
#         return render(request, 'goods/add_prod.html', context=data)

#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         data = {
#         'title':'Добавление товара',
#         'form':form   

#             }
#         return render(request, 'goods/add_prod.html', context=data)

def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
        # handle_uploaded_file(request.FILES['file_upload'])
    else:
        form = UploadFileForm()
    data = {
        'title': 'О сайте',
        'form': form,


    }
    return render(request, 'goods/about.html', context=data)

