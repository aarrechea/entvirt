""" Imports """
from django.contrib import admin
from django.urls import path, include



""" Patterns """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj_puro/', include('dj_puro.urls')),
    path('api/', include('api.urls')),
]
