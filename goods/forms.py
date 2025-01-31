from django import forms
from .models import Category

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255,label='Имя')
    content = forms.CharField(widget=forms.Textarea(), required=False,label='Описание')
    status = forms.BooleanField(required=False,initial=True,label='Статус')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Без категории',label='Категория')
