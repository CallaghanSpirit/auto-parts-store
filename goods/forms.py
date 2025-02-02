from django import forms
from .models import Category

from django.core.exceptions import ValidationError

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255,min_length=5,label='Имя',error_messages={'min_length': 'Слишком короткое название'})
    # slug = forms.SlugField(label='Слаг')
    desc = forms.CharField(widget=forms.Textarea(), required=False,label='Описание')
    status = forms.BooleanField(required=False,initial=True,label='Статус')
    cats = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Без категории',label='Категория')

    def clean_name(self):
        name = self.cleaned_data['name']
        message = 'Дебил'
        if not name.istitle():
           raise ValidationError(message)