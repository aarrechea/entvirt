""" Imports """
from django.urls import path
from api.apiView import (
    ProductoList, ProductoDetail, CategoriaSave, SubcategoriaSave, CategoriaList, 
    SubcategoriaList, CategoriaDetail, SubcategoriaAdd, ProductoViewset, UserCreate, LoginView)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls



""" Router """
router = DefaultRouter()
router.register("v2/producto", ProductoViewset, basename='producto')



""" Swagger initialization """
schema_view = get_swagger_view(title='Restful api curso DRF')



""" Patterns """
urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetail.as_view(), name='producto_detail'),
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_list'),
    #path('v1/subcategorias/', SubcategoriaList.as_view(), name='subcategoria_list'),
    path('v1/categorias/<int:pk>', CategoriaDetail.as_view(), name='categoria_detail'),
    path('v1/categoria/<int:pk>/subcategoria/', SubcategoriaList.as_view(), name='subcategoria_list' ),
    path('v1/categoria/<int:cat_pk>/addsubcategoria/', SubcategoriaAdd.as_view(), name='subcategoria_add' ),    
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),
    path("v4/login/", LoginView.as_view(), name="login"),
    path("v4/login-drf/", views.obtain_auth_token, name="login-drf"),
    path('swagger-docs', schema_view),
    path('coreapi-docs', include_docs_urls(title="Core api")),
]



urlpatterns += router.urls




