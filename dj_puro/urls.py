""" Imports """
from django.urls import path
from .views import categoria_detail, categoria_list



""" Patterns """
urlpatterns = [
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/<int:pk>/', categoria_detail, name='categoria_detail'),
]




