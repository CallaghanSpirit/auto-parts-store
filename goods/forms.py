from django import forms
from .models import Goods, Category

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





    # валидация поля
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     message = 'Дебил'
    #     if not name.istitle():
    #        raise ValidationError(message)