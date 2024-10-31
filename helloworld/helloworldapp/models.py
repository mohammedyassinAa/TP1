from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nom
