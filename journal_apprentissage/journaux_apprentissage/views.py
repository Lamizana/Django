from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Page d'accueil pour Journal d'apprentissage."""
    return render(request, 'journaux_apprentissage/index.html')


def topics(request):
    """Afficher tous les sujets."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'journaux_apprentissage/topics.html', context) 


def topic(request, topic_id):
    """Afficher un seul sujet et toutes ses entrées."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'journaux_apprentissage/topic.html', context)


def new_topic(request):
    """Ajouter un nouveaux sujet."""
    if request.method != 'POST':
        # Aucune données soumise, créer un formulaire vierge:
        form = TopicForm()
    else:
        # Donnees POST soumises, les traiter:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journaux_apprentissage:topics')
        
    # Affiche un formulaire vierge ou invalide:
    context = {'form': form}
    return render(request, 'journaux_apprentissage/new_topic.html', context)


def new_entry(request, topic_id):
    """Ajouter une nouvelle entrée a un sujet precis."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Aucune données soumise, créer un formulaire vierge:
        form = EntryForm()
    else:
        # Donnees POST soumises, les traiter:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('journaux_apprentissage:topic', topic_id=topic_id)

    # Affiche un formulaire vierge ou invalide:
    context = {'topic': topic, 'form': form}
    return render(request, 'journaux_apprentissage/new_entry.html', context)
         

def edit_entry(request, entry_id):
    """Modifier une entrée existante."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Requete initiale, remplir le formulaire avec l'entrée actuelle:
        form = EntryForm(instance=entry)
    else:
        # Donnees POST soumises, les traiter:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journaux_apprentissage:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'journaux_apprentissage/edit_entry.html', context)
        