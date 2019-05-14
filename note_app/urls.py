from django.urls import path

from .views import category_list_create, category_delete

app_name = 'note_app'

urlpatterns = [
    path('category/', category_list_create, name='category-list-create'),
    path('category/<int:pk>/delete', category_delete, name='category-delete'),
]
