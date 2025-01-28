from django.contrib import admin
from .models import Goods, Category
# Register your models here.

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'status', 'brief_info')
    list_display_links = ('name',)
    ordering = ['time_create', 'name']
    list_editable = ("status",)
    actions = ['set_status']
    search_fields = ['name']
    list_filter = ['status']

    @admin.display(description='Краткое описание', ordering='desc')
    def brief_info(self, goods:Goods):
        if len(goods.desc) > 0:
          return f"Описание {len(goods.desc)} символов"
        
    @admin.action(description='Опубликовать')
    def set_status(self, request, queryset):
        count = queryset.update(status=Goods.Status.IN_STOCK)
        self.message_user(request, f"Изменено {count} записей")

@admin.register(Category)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# admin.site.register(Goods, WomenAdmin)