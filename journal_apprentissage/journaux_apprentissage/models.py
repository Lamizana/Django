from django.db                  import models
from django.contrib.auth.models import User

# Creation des modéles.
class Topic(models.Model):
    """Sujet sur lequel l'utilisateur se documente."""
    
    # Stocke le nom du topic (max: 200 caracteres):
    text = models.CharField(max_length=200)
    # Fixe automatiquement l'heure courante lors de la creation d'un nv sujet:
    date_added = models.DateTimeField(auto_now_add=True)
    # Supprime tous les éléments liées a l'utilisateur:
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne une representation textuelle du modele."""
        return self.text
    
class Entry(models.Model):
    """Une information apprise sur le sujet."""
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # Stocke du texte (taille indéfinie gerée):
    text = models.TextField()
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Retourne une representation textuelle des 50 premiers mots."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text