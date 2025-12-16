from django.db import models

class TauxAT(models.Model):
    valeur = models.DecimalField(max_digits=10, decimal_places=2)
    date_effet = models.DateTimeField(auto_now_add=True)