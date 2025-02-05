from django.urls import path
from goods import views

urlpatterns = [
    path("",views.GoodsHome.as_view(), name='home'),
    path("card-page/<slug:gd_slug>/",views.cardpage,name='card-page'),
    path("category/<slug:cat_slug>",views.category, name='cat'),
    path('tag/<slug:tag_slug>/', views.show_tag, name='tag'),
    path('add-prod/', views.AddProd.as_view(), name='add-prod'),
    path('about/', views.about, name='about'),

]