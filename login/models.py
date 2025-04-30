from django.db import models

# Create your models here.


#Modelo de Usuario no banco.
class user(models.Model):
    usuario = models.CharField(max_length = 100)
    email = models.EmailField()
    senha = models.IntegerField()

    def __str__(self):
        return self.usuario
    