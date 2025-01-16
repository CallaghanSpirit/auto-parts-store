from django.urls import path
from goods import views

urlpatterns = [
    path("",views.index, name='home'),
    path("card-page/<slug:gd_slug>/",views.cardpage,name='card-page'),
    path("category/<slug:cat_slug>",views.category, name='cat')
]