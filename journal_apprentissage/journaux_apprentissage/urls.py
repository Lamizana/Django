"""Definir des motifs d'URL pour journaux_apprentissage"""

from django.urls    import path
from .              import views

app_name = 'journaux_apprentissage'

urlpatterns = [
    # Page d'accueil:
    path('', views.index, name='index'),

    # Page d'affichage de touts les sujets.
    path('topics/', views.topics, name='topics'),

    # Page d'affichage des détails d'un seul sujet.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page d'ajout d'un nouveau sujet.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page d'ajout d'une nouvelle entrée.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page de modification d'une entrée.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]