from django.contrib import admin

# Register your models here.
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published_date', 'category', 'image')
    list_display_links = ('title',  )
    search_fields = ('title', 'content', 'published_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category',]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)