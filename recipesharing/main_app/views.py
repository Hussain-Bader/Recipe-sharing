from django.shortcuts import render, redirect
from .models import Recipe , Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RecipeForm
# Create your views here.

class RecipeCreate(CreateView):
    model=Recipe
    form_class = RecipeForm

class RecipeUpdate(UpdateView):
    model=Recipe
    form_class = RecipeForm

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

def add_category(request, recipe_id):
    category_id = request.POST.get('category')
    Recipe.objects.get(id=recipe_id).categories.add(category_id)
    return redirect('detail', recipe_id=recipe_id)

def assoc_category(request, recipe_id, category_id):
    Recipe.objects.get(id=recipe_id).categories.remove(category_id)
    return redirect('detail', recipe_id=recipe_id)

def unassoc_category(request, recipe_id, category_id):
    Recipe.objects.get(id=recipe_id).categories.remove(category_id)
    return redirect('detail', recipe_id=recipe_id)