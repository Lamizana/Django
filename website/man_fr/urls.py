"""Definir des motifs d'URL pour journaux_apprentissage"""

from django.urls    import path
from .              import views

app_name = 'man_fr'

urlpatterns = [
    # Page d'accueil:
    path('', views.index, name='index'),

    # Page d'affichage de touts les sujets.
    path('topics/', views.topics, name='topics'),

     # Page d'affichage des détails d'un seul sujet.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]