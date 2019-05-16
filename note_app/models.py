from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField


User = get_user_model()


class Category(models.Model):
    """Model of category"""

    name = models.CharField('category name', max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    """Model of note"""

    name = models.CharField('note name', max_length=100)
    content = HTMLField('Content')
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
