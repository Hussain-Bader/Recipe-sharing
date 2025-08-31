from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'description', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            
        }