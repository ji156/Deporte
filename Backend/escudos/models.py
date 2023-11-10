from django.db import models

# Create your models here.


class EscudosLaLiga(models.Model):
    nombre = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='escudos/laliga')

    def __str__(self):
        return self.nombre


class EscudosPremier(models.Model):
    nombre = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='escudos/premier')

    def __str__(self):
        return self.nombre


class EscudosSeriea(models.Model):
    nombre = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='escudos/seriea')

    def __str__(self):
        return self.nombre


class EscudosBundesliga(models.Model):
    nombre = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='escudos/bundesliga')

    def __str__(self):
        return self.nombre


class EscudosLigue1(models.Model):
    nombre = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='escudos/ligue1')

    def __str__(self):
        return self.nombre
