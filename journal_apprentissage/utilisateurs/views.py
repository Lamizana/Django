from django.shortcuts           import render, redirect
from django.contrib.auth        import login
from django.contrib.auth.forms  import UserCreationForm

# Create your views here.
def register(request):
    """Inscrire un nouvel utilisateur."""
    if request.method != 'POST':
        # Afficher un formulaire d'inscription vide:
        form = UserCreationForm()
    else:
        # Traiter le formulaire rempli:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Ouvrir session de l'utilisateur et diriger vers la page accueil:
            login(request, new_user)
            return redirect('journaux_apprentissage:index')
        
    # Afficher un formuliare vierge ou invalide:
    context = {'form': form}
    return render(request, 'registration/register.html', context)
            