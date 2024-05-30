"""Définir des motifs d'urls pour utilisateur"""

from django.urls    import path, include
from .              import views

app_name = 'utilisateurs'

urlpatterns = [
    # Inclure les URL d'auhtentification par défault:
    path('',include('django.contrib.auth.urls')),
    
    # Page d'inscription:
    path('register/', views.register, name='register'),
]