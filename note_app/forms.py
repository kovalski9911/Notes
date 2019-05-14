from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    """Form for create category"""

    class Meta:
        model = Category
        fields = ['name']

        widgets = {'author': forms.HiddenInput()}
