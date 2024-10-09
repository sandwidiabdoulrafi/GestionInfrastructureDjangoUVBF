from django.db import models

# Create your models here.


# je vais creer une class de Administration avec ses attributs
class Administration(models.Model):
    Id_admin = models.AutoField(primary_key=True)
    adminNom = models.CharField(max_length=255)
    adminPrenom = models.CharField(max_length=255)
    adminEmail = models.EmailField(max_length=255)
    adminTel = models.CharField(max_length=15)
    adminMotPass = models.CharField(max_length=128, null=True, blank=True)
    
    def __str__(self):
        return f" Nom: {self.adminNom}  Prenom: {self.adminPrenom}"

class Infrastructures(models.Model):
    Id_Infratrs = models.AutoField(primary_key=True)
    infratsNom = models.CharField(max_length=255)
    infratsLocalition = models.CharField(max_length=255)
    infratsDescrip = models.CharField(max_length=300)
    infratsEtat = models.CharField(max_length=30)
    infratsDateEnrg = models.DateField(auto_now_add=True)
    Id_admin = models.ForeignKey(Administration, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Infrastructures {self.infratsNom} Description :  {self.infratsDescrip} Etat: {self.infratsEtat} Enregistrer: {self.infratsDateEnrg}"
    


class Interventions(models.Model):
    Id_Intertns = models.AutoField(primary_key=True)
    intertnsDate = models.DateField(null=True)
    Id_Infratrs = models.ForeignKey(Infrastructures, on_delete=models.CASCADE)

#Id_admin = models.ForeignKey(Administration, null=True, blank=True, on_delete=models.CASCADE)
