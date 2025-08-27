from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    ingredients = models.TextField(max_length=200)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})
