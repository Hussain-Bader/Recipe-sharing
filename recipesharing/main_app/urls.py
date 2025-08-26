from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes_index , name='index'),
    path('recipess/<int:recipe_id>/', views.recipes_detail, name='detail')
]