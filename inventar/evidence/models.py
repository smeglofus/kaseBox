from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Polozky(models.Model):
    BOX = "Box"
    PRISLUSENSTVI = "Příslušenství"
    OSTATNI = "Ostatní"

    kategorie = [(BOX, "Box"),(PRISLUSENSTVI, "Příslušenství"), (OSTATNI, "Ostatní")]
    typ = models.CharField(max_length=30, choices=kategorie, default=BOX)

    nazev = models.TextField(max_length=100, blank=False)
    poznamka = models.TextField(max_length=200, blank=True)
    



    def __str__(self):
        return self.nazev