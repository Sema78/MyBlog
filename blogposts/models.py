from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100, default="Uncategorized")

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
