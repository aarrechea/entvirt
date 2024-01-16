""" Imports """
from rest_framework import permissions



""" Owner class """
class IsOwner(permissions.BasePermission):
    message="No es propietario"
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user == obj.owner

