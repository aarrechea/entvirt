""" Imports """
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Categoria



""" List categories """
def categoria_list(request):    
    cat = Categoria.objects.all()[:20]
    data = {'results':list(cat.values('description', 'activo'))}
    return JsonResponse(data)


def categoria_detail(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {'result': 
                {
                    'description':cat.description,
                    'activo':cat.activo,
                }   
            }
    
    return JsonResponse(data)



