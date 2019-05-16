from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.exceptions import PermissionDenied

from .models import Category, Note
from .forms import CategoryForm, NoteForm

User = get_user_model()


class CategoryNoteListView(LoginRequiredMixin, CreateView):
    """Class for Note list, Categories list and for create note"""
    model = Note
    template_name = 'note_app/base.html'
    success_url = reverse_lazy('note_app:category-list')

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryNoteListView, self).get_context_data(*args, **kwargs)

        user = get_object_or_404(User, email=self.request.user)
        context['category_list'] = Category.objects.filter(author=user).order_by('-created')

        category_pk = self.kwargs.get('category_pk', None)
        if category_pk:
            category = get_object_or_404(Category, id=self.kwargs.get('category_pk'))
            if user == category.author:
                category_id = category.pk
                context['notes'] = Note.objects.filter(category__id=category_id)
            else:
                raise PermissionDenied

        return context

    def get_form(self, form_class=None):
        if self.request.method == 'POST':
            my_form = NoteForm(self.request.POST)
            if my_form.is_valid():
                return my_form
        else:
            my_form = NoteForm()
            user = self.request.user
            my_form.fields['category'].queryset = Category.objects.filter(author=user)
            return my_form


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """Class for create category"""

    model = Category
    form_class = CategoryForm
    template_name = 'note_app/category_create.html'
    success_url = reverse_lazy('note_app:category-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def category_delete(request, pk):
    """Delete Category function"""

    category = get_object_or_404(Category, pk=pk)
    if request.user == category.author:
        category.delete()
        return redirect('note_app:category-list')
    else:
        raise PermissionDenied


@login_required
def note_delete(request, pk):
    """Delete Note function"""
    note = get_object_or_404(Note, pk=pk)
    user = request.user
    category = note.objects.filter(category__author=user).first()
    if request.user == category.author:
        note.delete()
        return redirect('note_app:category-list')
    else:
        raise PermissionDenied
