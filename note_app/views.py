from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Category, Note
from .forms import CategoryForm, NoteForm

User = get_user_model()


class CategoryNoteListView(CreateView):
    """Class for Note list, Categories list and for create note"""
    model = Note
    form_class = NoteForm
    template_name = 'note_app/base.html'
    success_url = reverse_lazy('note_app:category-list')

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryNoteListView, self).get_context_data(*args, **kwargs)

        user = get_object_or_404(User, email=self.request.user)
        context['category_list'] = Category.objects.filter(author=user).order_by('-created')

        if self.kwargs:
            category = get_object_or_404(Category, id=self.kwargs.get('category_pk'))
            category_id = category.pk
            context['notes'] = Note.objects.filter(category__id=category_id)
        return context


class CategoryCreateView(CreateView):
    """Class for create category"""
    model = Category
    form_class = CategoryForm
    template_name = 'note_app/category_create.html'
    success_url = reverse_lazy('note_app:category-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def category_delete(request, pk):
    """Delete Category function"""
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('note_app:category-list')


def note_delete(request, pk):
    """Delete Note function"""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_app:category-list')
