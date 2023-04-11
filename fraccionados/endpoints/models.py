from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    grado = models.IntegerField()
    grupo = models.CharField(max_length=1)
    rol= models.CharField(max_length= 10)

class Estadisticas_por_intento(models.Model):
    id = models.IntegerField(primary_key=True) #lo pongo relacionado al id de usuario
    numero_nivel = models.IntegerField()
    tematica_nivel = models.CharField(max_length=12)
    puntuacion = models.IntegerField()
    tiempo_juego = models.CharField(max_length=15) #no hay fecha, por mientas lo pongo como texto
    porcentaje_dominio = models.IntegerField()

class Roles(models.Model):
    id = models.IntegerChoices(primary_key=True)
    estudiante = models.BooleanField() #son texto en el sqlite3
    administrador = models.BooleanField()
    profesor = models.BooleanField()