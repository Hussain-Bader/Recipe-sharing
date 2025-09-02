from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes_index , name='index'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),

    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_comment/', views.add_comment, name='add_comment'),
    path('recipes/<int:recipe_id>/add_category/', views.add_category, name='add_category'),
    path('recipes/recipes_list', views.recipe_list, name='recipes_list'),
    path('accounts/signup/', views.signup , name='signup')
]