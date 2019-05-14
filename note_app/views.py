from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import UpdateView

from .models import Category
from .forms import CategoryForm

User = get_user_model()


def category_list_create(request):
    """List Category and Create Category function"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('note_app:category-list-create')
    else:
        user = get_object_or_404(User, email=request.user)
        category_list = Category.objects.filter(author=user).order_by('-created')
        form = CategoryForm()
        context = {
            'form': form,
            'category_list': category_list
        }
        return render(request, 'note_app/category_list.html', context)


def category_delete(request, pk):
    """Delete Category function """
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('note_app:category-list-create')
