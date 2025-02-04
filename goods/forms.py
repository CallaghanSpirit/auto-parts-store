from django import forms
from .models import Goods, Category
from pathlib import Path

from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    cats = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Без категории',label='Категория')
    class Meta:
        model = Goods
        fields = ["name", "desc", "cats","status"]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'desc': forms.Textarea(attrs={'cols': 50, 'rows':5}),
        }
        labels = {'desc': 'Описание'}

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')

    # def clean_file(self):
    #     file = self.cleaned_data['file']
    #     path = Path(f'uploads/{file}')
    #     if path.is_file():
    #         raise ValidationError('Файл уже существует')




    # валидация поля
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     message = 'Дебил'
    #     if not name.istitle():
    #        raise ValidationError(message)