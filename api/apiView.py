""" Imports """
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto, Categoria, Subcategoria
from .serializer import ProductoSerializer, CategoriaSerializer, SubcategoriaSerializer, UserSerializer
from rest_framework import viewsets
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated



""" Producto """
""" class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()[:10]
        data = ProductoSerializer(prod, many=True).data
        return Response(data)
    
    
Detail
class ProductoDetail(APIView):
    def get(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data) """

    
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    
class ProductoDetail(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaSave(generics.CreateAPIView):
    serializer_class = CategoriaSerializer
    
    
class SubcategoriaSave(generics.CreateAPIView):
    serializer_class = SubcategoriaSerializer
    
        
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
""" class SubcategoriaList(generics.ListCreateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer """


class CategoriaDetail(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    
class SubcategoriaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Subcategoria.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = SubcategoriaSerializer
    
    
class SubcategoriaAdd(APIView):
    def post(self, request, cat_pk):
        descripcion = request.data.get('descripcion')
        data = {
            'categoria':cat_pk, 
            'descripcion':descripcion
            }
        
        serializer = SubcategoriaSerializer(data=data)
        if serializer.is_valid():
            subcat = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = ([IsAuthenticated, IsOwner])
    
    
class UserCreate(generics.CreateAPIView):
    # Invalidating global settings
    authentication_classes = () 
    permission_classes = ()
    
    serializer_class = UserSerializer    


class LoginView(APIView):
    permission_classes = ()
            
    def post(self, request):        
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"token":user.auth_token.key})
        else:
            return Response({"error":"Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
        

        
