from rest_framework import serializers

from AppGestionInfrastructure.models import Administration, Infrastructures, Interventions


# serializer permet la conversion des instances des modèles Django en JSON (ou un autre format) pour l'API, et inversement


# creation d'une class CitoyenSerializer pour definire les pouvoir du citoyen ici on veux q'il ai acces limiter au attributs de 
#la la table Infrastructures pour lui permettre seulement l'enregisttrement ,et la modification .



class CitoyenSerializer(serializers.ModelSerializer):

    class Meta :

        model = Infrastructures

        fields = ('infratsNom', 'infratsLocalition','infratsDescrip','infratsEtat','infratsDateEnrg') 
        






class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta :
        model = Infrastructures
        fields = ('infratsNom', 'infratsLocalition','infratsDescrip','infratsEtat','infratsDateEnrg')


class InterventionsSerializerdos(serializers.ModelSerializer):
    
    class Meta:
        model = Interventions
        fields = ('Id_Intertns', 'intertnsDate','Id_Infratrs')
        





class InfrastructureSerializerDos(serializers.ModelSerializer):
    # Champ personnalisé pour obtenir les informations de l'infrastructure associée
    infrastructure = serializers.SerializerMethodField()

    class Meta:
        model = Interventions
        fields = ['intertnsDate','infrastructure']  # Champs retournés par le serializer

    def get_infrastructure(self, obj):
        # Vérifie que l'intervention est associée à une infrastructure
        if obj.Id_Infratrs:
            return {
                'infratsNom': obj.Id_Infratrs.infratsNom,
                'infratsLocalition': obj.Id_Infratrs.infratsLocalition,
                'infratsDescrip': obj.Id_Infratrs.infratsDescrip,
                'infratsEtat': obj.Id_Infratrs.infratsEtat,
                'infratsDateEnrg': obj.Id_Infratrs.infratsDateEnrg,
                'intertnsDate': obj.intertnsDate
            }
        return None  # Retourne None si aucune infrastructure n'est associée





class InterventionsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Interventions
        fields= ('Id_Infratrs','intertnsDate')


class CityenSerializer(serializers.ModelSerializer):
    intertnsDate = serializers.DateField(source='intervension.intertnsDate', read_only=True) 
    class Meta :
        model = Infrastructures
        fields = ('infratsNom', 'infratsLocalition','infratsDescrip','infratsEtat','infratsDateEnrg', 'intertnsDate', 'intertnsDate')
        
    def create (self, dataValide):
        Infrastructures.objects.create(**dataValide)

    def update(self, instance, dataValide):
        instance.infratsNom = dataValide.get('infratsNom',instance.infratsNom)
        instance.infratsLocalition = dataValide.get('infratsLocalition',instance.infratsLocalition)
        instance.infratsDescrip = dataValide.get('infratsDescrip',instance.infratsDescrip)
        instance.infratsEtat = dataValide.get('infratsEtat',instance.infratsEtat)
        instance.infratsDateEnrg = dataValide.get('infratsDateEnrg',instance.infratsDateEnrg)
        instance.save()
        return instance


# creation de d'une class AdministrationSerializer pour lui permetre d'avoir acces au a la table Infrastructures et  Interventions
# en  lui permetant a la modification , enregistrement, suppression et aussi valide une date d'intervention



class AdministrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Administration
        fields = ('adminNom','adminPrenom', 'adminEmail','adminTel','adminMotPass')
    


#class AdministrationSerializer(serializers.ModelSerializer):
    
    #la gestion de intervention

    #intervention = InterventionsSerializer(many=True,required=False)

    # class Meta:
    #     model = Administration
    #     fields = ('adminNom','adminNom', 'adminEmail','adminTel','adminMotPass')

    # def create(self, dataValide):
    #     interventionsData = dataValide.pop('interventions', [])
    #     infrastructuresData = Infrastructures.objects.create(**dataValide)

    #     for interventions_Data in interventionsData:
    #         #Creation d'une clé dans intervention pour associer au une infrastructure

    #         Interventions.objects.create(Id_Infratrs= infrastructuresData, **interventions_Data)

    #     return infrastructuresData


    # def update(self, instance, dataValide):

    #     instance.infratsNom = dataValide.get('infratsNom', instance.infratsNom)
    #     instance.infratsLocalition = dataValide.get('infratsLocalition', instance.infratsLocalition)
    #     instance.infratsDescrip = dataValide.get('infratsDescrip', instance.infratsDescrip)
    #     instance.infratsEtat = dataValide.get('infratsEtat', instance.infratsEtat)
    #     instance.infratsDateEnrg = dataValide.get('infratsDateEnrg', instance.infratsDateEnrg)
    #     instance.save()

    #     interventionsData = dataValide.pop('interventions', [])

    #     for interventions_Data in interventionsData:
    #         IdOfIntertns = interventions_Data.get('Id_Intertns', None)

    #         if(IdOfIntertns):
    #             #verification de L'esxistance de L'id de la date d'intervension on porte une modification de L'etat
    #             intervention = Interventions.objects.get(Id_Intertns = IdOfIntertns,Id_Infratrs = instance)
    #             intervention.intertnsDate = interventions_Data.get('intertnsDate',intervention.intertnsDate)
    #             intervention.save()

    #         else:
    #             # sinon creer un 
    #             Interventions.objects.create(Id_Infratrs = instance, **interventions_Data)

    #     return instance























# class InterventionsSerializer(serializers.ModelSerializer):
#     class Meta :
#         model = Interventions
#         fields= ('intertnsDate',)