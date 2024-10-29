from django.db import models

class Actividad(models.Model):
    nombre = models.CharField(max_length=255)
    tiempo_optimista = models.IntegerField()
    tiempo_medio = models.IntegerField()
    tiempo_pesimista = models.IntegerField()
    Json = models.JSONField()
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
