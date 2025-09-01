from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    cats = Category.objects.all()
    CATEGORIES = (('B', 'Main dish'), ('A', 'Appetizer'), ('D', 'Dessert'), ('S', 'Snack'))
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    ingredients = models.TextField(max_length=200)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

