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
    path('recipes/<int:recipe_id>/assoc_category/<int:category_id>/',views.assoc_category, name='assoc_category'),
    path('recipes/<int:recipe_id>/unassoc_category/<int:category_id>/',views.unassoc_category, name='unassoc_category')
]