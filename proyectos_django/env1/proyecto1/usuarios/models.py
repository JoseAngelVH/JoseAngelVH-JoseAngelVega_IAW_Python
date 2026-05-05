from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    km1 = models.IntegerField()
    km2 = models.IntegerField()
    km3 = models.IntegerField()
    km4 = models.IntegerField()
    km5 = models.IntegerField()
    km6 = models.IntegerField()
    km7 = models.IntegerField()
    km8 = models.IntegerField()
    km9 = models.IntegerField()
    km10 = models.IntegerField()

    def __str__(self):
        return self.nombre
