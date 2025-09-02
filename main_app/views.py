from django.shortcuts import render, redirect
from .models import Recipe , Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RecipeForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class RecipeCreate(LoginRequiredMixin,CreateView):
    model=Recipe
    form_class = RecipeForm
    
    def form_valid(self , form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin,UpdateView):
    model=Recipe
    form_class = RecipeForm


class RecipeDelete(LoginRequiredMixin,DeleteView):
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

@login_required
def add_comment(request, recipe_id):
    content = request.POST.get('content')
    new_comment = Comment(content=content, recipe_id=recipe_id,user=request.user)
    new_comment.save()
    return redirect('detail', recipe_id =recipe_id)


def add_category(request, recipe_id):
    category_id = request.POST.get('category')
    Recipe.objects.get(id=recipe_id).categories.add(category_id)
    return redirect('detail', recipe_id=recipe_id)


def recipe_list(request):
    query = request.GET.get("q")
    recipes = Recipe.objects.all()

    if query:
        
        recipes = recipes.filter(
            Q(title__icontains=query) | 
            Q(category__in=[key for key, label in Recipe.CATEGORIES if query.lower() in label.lower()])
        )

    return render(request, "recipes/recipes_list.html", {"recipes": recipes})

def signup(request):
    error_message = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup - Try Again...'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)