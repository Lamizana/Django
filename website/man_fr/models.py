from django.db import models

# Create your models here.
class Topic(models.Model):
    """Sujet du man sur lequel l'utilisateur se documente."""
    text = models.CharField(max_length=200)
    """Fixe automatiquement l'heure courante lors de la creation d'un nv sujet."""
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retourne une representation textuelle du modele."""
        return self.text
    
class Entry(models.Model):
    """Une information apprise sur le sujet."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


    name = models.CharField(max_length=200)
    synopsis = models.TextField()
    description = models.TextField()
    auteur = models.CharField(max_length=200)
    bug = models.TextField()
    copyright = models.TextField()
    also = models.TextField()


    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Retourne une representation textuelle des 50 premiers mots."""
        if len(self.name) > 50:
            return f"{self.name[:50]}..."
        return self.name