from django.db import models
from django.contrib.auth.models import User # Added

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
            return self.title

class Category(models.Model):

    # name
    name = models.CharField(max_length=128)
    # description
    description = models.TextField(blank=True)
    # posts, one post can have many categories and one category can have many posts 
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name_plural = 'categories'
