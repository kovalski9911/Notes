from django import forms

from .models import Category, Note


class CategoryForm(forms.ModelForm):
    """Form for create category"""

    class Meta:
        model = Category
        fields = ['name']

        widgets = {'author': forms.HiddenInput()}


class NoteForm(forms.ModelForm):
    """Form for create note"""

    class Meta:
        model = Note
        fields = ['name', 'content', 'category']
