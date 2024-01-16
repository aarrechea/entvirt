""" Imports """
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Producto, Categoria, Subcategoria
from django.contrib.auth.models import User



""" Producto serializer """
class ProductoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Producto
        fields = '__all__'


""" Categoria serializer """
class CategoriaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Categoria
        fields = '__all__'
        
        
""" Subcategoria serializer """        
class SubcategoriaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Subcategoria
        fields = '__all__'


""" User serializer """
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        


