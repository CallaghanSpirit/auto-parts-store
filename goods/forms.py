from django import forms
from .models import Category

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    status = forms.BooleanField(required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
