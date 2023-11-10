from django.db import models

# Create your models here.
class Karty(models.Model):
    VCU = "VCU"
    DIAG = "DIAG"
    TCN = "TCN"
    ETH = "ETH"
    CANNODE = "CANNODE"

    typ_volba = [(VCU, "VCU"),(DIAG, "DIAG"), (TCN, "TCN"), (ETH, "ETH"), (CANNODE, "CANNODE")]
    typ = models.CharField(max_length=20, choices=typ_volba, default=VCU)
    cislo = models.IntegerField(max_length=40, default=0)
    verze = models.FloatField(max_length=5)
    poznamka = models.TextField(max_length=200, blank=True)
    

    def __str__(self):
        return self.typ + " " + str(self.verze) + " Číslem:  " + str(self.cislo)