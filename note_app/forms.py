from django import forms
from tinymce import TinyMCE

from .models import Category, Note

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class CategoryForm(forms.ModelForm):
    """Form for create category"""

    class Meta:
        model = Category
        fields = ['name']

        widgets = {'author': forms.HiddenInput()}


class NoteForm(forms.ModelForm):
    """Form for create note"""

    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Note
        fields = ['name', 'content', 'category']
