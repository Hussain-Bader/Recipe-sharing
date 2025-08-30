from django.shortcuts import render, redirect
from .models import Recipe , Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class RecipeCreate(CreateView):
    model=Recipe
    fields=['title','ingredients','description','image']

class RecipeUpdate(UpdateView):
    model=Recipe
    fields=['title','ingredients','description']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'

def home(request):
    return render(request, 'home.html')

def recipes_index(req):
    recipes = Recipe.objects.all()
    return render(req,'recipes/index.html' , {'recipes': recipes})

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', { 'recipe': recipe })

def add_comment(request, recipe_id):
    content = request.POST.get('content')
    new_comment = Comment(content=content, recipe_id=recipe_id)
    new_comment.save()
    return redirect('detail', recipe_id=recipe_id)
