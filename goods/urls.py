from django.urls import path
from goods import views

urlpatterns = [
    path("",views.index, name='home'),
    path("category/",views.category, name='cats')
]