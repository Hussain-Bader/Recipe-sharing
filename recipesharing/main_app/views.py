from django.shortcuts import render
from .models import Recipe
# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello Cat Collector</h1>')
    return render(request, 'home.html')

def recipes_index(req):
    recipes = Recipe.objects.all()
    return render(req,'recipes/index.html' , {'recipes': recipes})