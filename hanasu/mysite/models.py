from django.db import models


# Create your models here.
# permets de créer des table dans la BDD avec les diférents champs inclus à l'interieur.

# Class Ideogramm contenant un champs : Name, Romanji, Img_link et Id_type_idéo permettant un 
# lien avec la table Ideotype.



class Ideogramm(models.Model):
    
    romanji = models.CharField(max_length=50, null=True)
    Img_link = models.CharField(max_length=100, null=True)
    # faire foreign pour joindre les types d'ideogramm
    

    def __str__(self):
        return f"{self.romanji}- {self.Img_link}"
    
class Ideotype(models.Model):
    Name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.Name}"
