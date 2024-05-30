from django.shortcuts import render
from .models import Topic

def index(request):
    """Page d'accueil pour man francais ZEHD."""
    return render(request, 'man_fr/index.html')

def topics(request):
    """Afficher tous les sujets."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'man_fr/topics.html', context) 

def topic(request, topic_id):
    """Afficher un seul sujet et toutes ses entrées."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'man_fr/topic.html', context)