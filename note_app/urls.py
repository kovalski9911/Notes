from django.urls import path

from .views import CategoryNoteListView, CategoryCreateView, category_delete, note_delete

app_name = 'note_app'

urlpatterns = [
    path('category/', CategoryNoteListView.as_view(), name='category-list'),
    path('category/create', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/delete', category_delete, name='category-delete'),
    path('category/<int:category_pk>', CategoryNoteListView.as_view(), name='notes-of-category-list'),
    path('notes/<int:pk>/delete', note_delete, name='note-delete'),
]
