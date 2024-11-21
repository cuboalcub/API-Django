from django.db import models

class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    Json = models.JSONField()
    imagen = models.TextField()  # Sin límite de longitud

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
