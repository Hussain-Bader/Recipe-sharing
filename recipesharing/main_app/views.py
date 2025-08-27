from django.shortcuts import render
from .models import Recipe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class RecipeCreate(CreateView):
    model=Recipe
    fields=['title','description','image','ingredients']

class RecipeUpdate(UpdateView):
    model=Recipe
    fields=['title','description','ingredients']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'

def home(request):
    # return HttpResponse('<h1>Hello Cat Collector</h1>')
    return render(request, 'home.html')

def recipes_index(req):
    recipes = Recipe.objects.all()
    return render(req,'recipes/index.html' , {'recipes': recipes})

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', { 'recipe': recipe })