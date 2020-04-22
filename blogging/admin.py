from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    fields = ('title', 'body', 'author', 'published_date')

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    fields = ('name', 'description')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


