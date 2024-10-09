import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.sessions.backends.db import SessionStore

from AppGestionInfrastructure.models import Administration, Infrastructures, Interventions
from AppGestionInfrastructure.serializers import CitoyenSerializer, InfrastructureSerializer, AdministrationSerializer, InfrastructureSerializerDos, InterventionsSerializerdos



@api_view(['GET', 'POST'])
def CitizenSaveInfrastruct(request):
    data = request.data.get('data')

    if request.method == 'POST':
        restruct_data = {
            'infratsNom': data.get('infrats'),
            'infratsLocalition': data.get('localisation'),
            'infratsDescrip': data.get('desciprtion'),
            'infratsEtat': data.get('etat'),
            'infratsDateEnrg': data.get('DateEnrg'),
        }

        # Obtenir l'instance si elle existe
        print('restruct_data : ', restruct_data)

        infras_exist = Infrastructures.objects.filter(infratsNom=restruct_data['infratsNom']).first()
        print('infras_exist : ', infras_exist)

        if infras_exist:
            # Mettre à jour si l'infrastructure existe
            serializer = InfrastructureSerializer(infras_exist, data=restruct_data)
            

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Infrastructure mise à jour avec succès !'}, status=200)
            else:
                return Response({'message': 'Erreur : sérialiseur d\'infrastructure invalide !'}, status=400)
            
        else:
            # Créer une nouvelle infrastructure si elle n'existe pas
            serializer = InfrastructureSerializer(data=restruct_data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Infrastructure enregistrée avec succès !'}, status=201)
            else:
                return Response({'message': 'Erreur : sérialiseur d\'infrastructure invalide !'}, status=400)










# @api_view(['GET','POST'])

# def CitizenSaveInfrastruct(request):
#     data = request.data.get('data')


#     if request.method =='POST':
#         restruction_data ={
#             'infratsNom': data.get('infrats'),
#             'infratsLocalition': data.get('localisation'),
#             'infratsDescrip': data.get('desciprtion'),
#             'infratsEtat': data.get('etat'),
#             'infratsDateEnrg': data.get('DateEnrg'),
#         }
        
#         infras_exist = Infrastructures.objects.filter(infratsNom=restruction_data['infratsNom']).exists()
#         print("infras_exist : ", infras_exist)
        
#         if infras_exist:
#             print("l'infrastucture existe déjà")

#             return Response({'messaige':"l'infrastucture existe déjà"},status=400)


#         else:

#             # serializer = CitoyenSerializer(data=restruction_data)  

#             # if serializer.is_valid():

#             #     serializer.save()

#             #     print('infrastructure enregistrer avec succè !')

#             #     return Response({'message':'infrastructure enregistrer avec succè !'})
            
#             # else:

#             #     print('Erreur serializer invalide')
#             print("l'infrastucture est enregistrer ")

#             return Response({'message':"l'infrastucture est enregistrer"})


       

        











#_-_-_-_-_-_-_-_-_-_-_-_-_- Les personnels se l'ADMINISTRATION_-_-_-_-_-_-_-_-_-_-_-_-_-



#=-=-=-=-=--=-=-=_________________authentification__________________-=-=-=-=-=-=-=-=-=-=





#________________connection___________________

@api_view(['GET','POST'])
def loginAdministration(request):
    if request.method == 'POST':

        data = request.data.get('data')

        restruction_data ={
            'adminEmail': data.get('email'),
            'adminMotPass': data.get('password')
        }
        
        useExist = Administration.objects.filter(adminEmail=restruction_data['adminEmail']).exists()

        if useExist:
            
            #on recuper ce information et on verifie le mot de passe
            userInfo = Administration.objects.filter(adminEmail=restruction_data['adminEmail']).first()
            
            #make_password

            password = restruction_data['adminMotPass']
        

            if check_password(password, userInfo.adminMotPass):

                #creation d'une session du personnel de l'administration
                
                #stokage de l'id de l'utilisateur dans la session 
                request.session['admin_id'] = userInfo.Id_admin
                request.session.save()

                response = JsonResponse({'message':'connexion réussi', 'id de la session':request.session.session_key}, status=201)
                response.set_cookie(request.session.session_key)

                return response

            else: 
                
                return JsonResponse({'message':'Mot de passe incorrect'}, status=400)


        else: 
            return  Response({'message': "l'utilisateur n'existe pas qu'il s'inscription"}, status=201)




#------------------------Creation de compte-----------------------------

@api_view(['GET','POST'])

def SignUpAdministration(request):

    
    if request.method == 'POST':

        #recuperation des données  pour inserer dans la variable data  

        data = data = request.data.get('data')
        hashPassword = make_password(data.get('password'))
        restruction_data =  {
            'adminNom': data.get('nom'),
            'adminPrenom': data.get('prenom'),
            'adminEmail': data.get('email'),
            'adminTel': data.get('tel'),
            'adminMotPass': hashPassword
        }

        # VIRIFIONS L'EXISTANTE de l'utilisateur avant la de l'inscrire

        user_exist = Administration.objects.filter(adminEmail=restruction_data['adminEmail']).exists()


        if user_exist:
            
            return  Response({'message': "l'utilisateur existe qu'il se connecte "}, status=201)

        else: 
            #creation d'une nouvelle instance pour le user
            serializer = AdministrationSerializer(data=restruction_data)

            print("-------------------------les data  de l'inscription reçuent sont : ",data)

            #verifions si les données sont valides  
            if serializer.is_valid():
                #si oui on creer le compte
                serializer.save()
                print("-----------------L'adminateur", restruction_data['adminNom']," est inscrit ---------------------------")
                return JsonResponse({"message": "Inscription de l'adminateur réussie !"}, status=201)
            else:
                #si non on retourne un erreur
                
                return JsonResponse({"message": "ERREUR lors de l'inscription de l'adminateur !", " Erreur " : serializer.errors }, status=400)
            


#________________déconnection___________________

@api_view(['GET','POST'])

def disconnection(request):
    #on verifie si la session est ouvert
    admin_id = request.session.get('admin_id')

    if admin_id is None:
        #  elle n'etait pas ouvert on signale qu'il etait pas connecter

        return Response({'message':'vous etes pas connecter'}, status=400)
    
    if request.method == 'POST':
        #oui si la sesion etait activer alors on l'arrete

        request.session.clear()
        return Response({'message':'déconnection réussi'}, status=400)






#-----------------------suppresion de compte---------------------------

@api_view(['GET','POST'])

def deleteAccount(request):
    admin_Id = request.session.get('admin_id')
    if admin_Id is None :

        return Response({'message':'suppresion refusé connecter vous '}, status=400)
    
    if request.method == 'POST':
        data = request.data.get('data')

        restruction_data ={
            'adminEmail': data.get('email'),
            'adminMotPass': data.get('password')
        }

        useAdministration = Administration.objects.get(adminEmail=restruction_data['adminEmail'])

        useAdministration.delete()
        request.session.clear()

        print('Votre copmte a été supprimer avec succè !!!')

        return Response({'message':'Votre copmte a été supprimer avec succè '}, status=201)
























#=-=-=-=-=--=-=-=_________________ authentification FIN__________________-=-=-=-=-=-=-=-=-=-=





#=-=-=-=-=--=-=-=__________________GESTION DU PERSONNEL __________________-=-=-=-=-=-=-=-=-=-=

#________________renvoyer tout les utilisateur___________________

@api_view(['GET','POST'])
def allUserAdministration(request):


    admin_id = request.session.get('admin_id')

    #verification des l'existance de la session du user de l'administration avant d'executer la requette 
    #et renvoyer la liste de tous les personnes de L'administration
    
    if admin_id is None:
        return JsonResponse({'error': 'vous etes pas  autorisé a executer cette requette'}, status=401)


    if request.method == 'POST':
        allUser = Administration.objects.values('adminNom','adminPrenom', 'adminEmail','adminTel')
        allUserSerializes = AdministrationSerializer(allUser,many=True)

        return JsonResponse({'data':allUserSerializes.data}, status=201)
    

#=-=-=-=-=--=-=-=__________________GESTION DU PERSONNEL  FIN __________________-=-=-=-=-=-=-=-=-=-=









#=-=-=-=-=--=-=-=__________________GESTION DES INFRASTRUCTURES __________________-=-=-=-=-=-=-=-=-=-=



#---------------------------obtention des infrastructure et leurs date d'intervention-------------------------------
#--------------------ADMINISTRATION && CITOYENS------

@api_view(['GET','POST'])

def getAllInfrastructureWithIntevensionDate(request):
    
    # CETTE FONCTION AUSSI VERIFIE SI C'EST UN PERSONNEL DE L'ADMINISTRATION AVANT DE DONNE SUITE A LA REQUETTE 

    # admin_id = request.session.get('admin_id')
    # if admin_id is None:

    #     #refusé l'access
    #     return JsonResponse({'error': 'vous etes pas  autorisé a executer cette requette'}, status=401)

    if request.method == 'POST':
        #recuperer tout les infrastructures
        infrastructures = Infrastructures.objects.all()

        print("-----------------infrastructures-------::::::", infrastructures)

        # puis les serialiser tous avant de retourner les infrastructure avec  leur date d'intervension

        infrastructuresSerialiser = InfrastructureSerializerDos(Interventions.objects.filter(Id_Infratrs__in=infrastructures),many=True)

        print("-----------------infrastructuresSerialiser.data-------::::::", infrastructuresSerialiser.data)

        return JsonResponse({'data':infrastructuresSerialiser.data}, safe=False, status=201)






#------------------mettre ajour la date seulemnent------------------------

#dedier a un boutton << planifier>>

@api_view(['GET','POST'])

def insertOneDataIntervention(request):

    admin_id = request.session.get('admin_id')
    if admin_id is None:

        #refusé l'access
        return JsonResponse({'error': 'vous etes pas  autorisé a executer cette requette'}, status=401)

    if request.method == 'POST':

        data = request.data.get('data')

        print("infastructure a ajouter la date est: ",data )

        restruction_data = {
                'infratsNom': data.get('infrats'),
                'intertnsDate': data.get('dateIntervention'),
        }

        #creation d'une instance pour insert la date de l'infrastructure
        intervention = Interventions()

        #recuperation de l'id de L'infrastructure concernet et mettre une date dans la cl, etrangère dans la 
        #la table de l'intervention
        idInfrastructure = Infrastructures.objects.filter(infratsNom=restruction_data['infratsNom']).first()
        
        intervention.Id_Infratrs = idInfrastructure

        #et on insert la date correspondant 

        intervention.intertnsDate = restruction_data['intertnsDate']
        #on sauvegarde l'instance 
        intervention.save()


        # on recuperer l'infrastructure et la date  pour renvoyer mais on va rien renvoyer plus précisement on renvoie 
        #message dire que la date a ete mise a jour
        # infrastructureSelect = Infrastructures.objects.filter(infratsNom=restruction_data['infratsNom'])
        # serializer = InfrastructureSerializerDos(Interventions.objects.filter(Id_Infratrs__in=infrastructureSelect), many=True)
        

        return Response({'message':"Planification Réussi"}, status=201)
    




    
#------------------------Enregistrer un infrastructure avec sa date planifier------------------------



@api_view(['GET','POST'])

def sauveInfrastructureWithDateInterventions(request):

    admin_id = request.session.get('admin_id')
    if admin_id is None:

        #refusé l'access
        return JsonResponse({'error': 'vous etes pas  autorisé a executer cette requette'}, status=401)

    if request.method == 'POST':

        print('------les data pour ajouter une infriastructure reçuent sont : ',request.data)

        data = request.data.get('data')
        restruction_data = {
                'infratsNom': data.get('infrats'),
                'infratsLocalition': data.get('localisation'),
                'infratsDescrip': data.get('desciprtion'),
                'infratsEtat': data.get('etat'),
                'infratsDateEnrg': data.get('DateEnrg'),
                'intertnsDate': data.get('dateIntervention')
        }
        infras_exist = Infrastructures.objects.filter(infratsNom=restruction_data['infratsNom']).exists()

        #on recupere le data et verifier l'existance de l'infrastructure avant l'insertion

        
        if infras_exist:
            #retourner une reponse disant que l'infrastructure existe
            print("----------------l'infrastructure existe déjà-----------------------")

            return  Response({'message': "l'infrastructure existe déjà"}, status=201)

        else:
            # creation d'une instance pour le InfrastructureSerializer d'infrastructure
            serializer = InfrastructureSerializer(data=restruction_data)

            if serializer.is_valid():

                #sauvegarder l'instance 
                serializer.save()

                # creation d'une instance intevensoin pour la sauvegarde  de la date d'intervention
                intervention = Interventions()

                idInfrastructure = Infrastructures.objects.filter(infratsNom=restruction_data['infratsNom']).first()

                intervention.Id_Infratrs = idInfrastructure

                intervention.intertnsDate = restruction_data['intertnsDate']
                intervention.save()

                print("----------------l'infrastructure ajouter avec succè -----------------------", serializer.errors)

                #ici on renvoyait tout les infrastructure et leur date d'intervention
                
                # infrastructures = Infrastructures.objects.all()
                # allInfrastructure = InfrastructureSerializerDos(Interventions.objects.filter(Id_Infratrs__in=infrastructures), many=True)

                # , "updateList":allInfrastructure.data
                
                return JsonResponse({"message": "l'infrastructure ajouter avec succè"}, status=201)
                

            else:

                print("ERREUR lors de l'insertion du l'infastructure Error: ", serializer.errors )


                return  Response({'message': "Erreur lors de l'insertion d'une nouvelle infrastructure"}, status=400)







#=-=-=-=-=--=-=-=__________________GESTION DES INFRASTRUCTURES FIN __________________-=-=-=-=-=-=-=-=-=-=






































# @api_view(['POST'])
# def user_signup(request):
#     if request.method == 'POST':
        
#         data = request.data.get('data')
#         restruction_data =  {
#             'adminEmail': data.get('email'),
#             'adminMotPass': data.get('mot de passe')
#         }


#         email = restruction_data['adminEmail']
#         password = restruction_data['adminMotPass']

#         # Vérifier si l'utilisateur existe déjà
#         if User.objects.filter(username=email).exists():
#             return JsonResponse({'error': 'Un utilisateur avec cet email existe déjà.'}, status=400)

#         # Créer un nouvel utilisateur
#         user = User.objects.create(
#             username=email,
#             email=email,
#             password=make_password(password)  # Hacher le mot de passe pour le stocker de manière sécurisée
#         )
#         user.save()

#         return JsonResponse({'message': 'Inscription réussie'}, status=201)












#_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-__-_-_- Is ok _-_-_-_-_-_-__-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_











                # idInfrast = Infrastructures.object.filter(infratsNom=restruction_data['infratsNom']).first()

                # serializerIntervention = InterventionsSerializer(data={'Id_Infratrs':idInfrast.id,'intertnsDate' : None})






































#-------------------------modifier seule men la date d'intervension-------------------_________--____________________




# @api_view(['GET','POST'])

# def programInterventionDate(request):

#     if request.method == 'POST':

#         data = request.data.get('data')

#         print("infastructure a ajouter la date est: ",data )

#         restruction_data = {
#                 'infratsNom': data.get('infrats'),
#                 'infratsLocalition': data.get('localisation'),
#                 'infratsDescrip': data.get('desciprtion'),
#                 'infratsEtat': data.get('etat'),
#                 'infratsDateEnrg': data.get('DateEnrg'),
#                 'intertnsDate': data.get('intertnsDate')
#         }


#         intervention = Interventions()
#         idInfrastructure = restruction_data['Id_Infratrs']
#         infrastructure = Infrastructures.objects.get(id=idInfrastructure)
#         intervention.Id_Infratrs = idInfrastructure
#         infrastructure.intertnsDate = restruction_data['dateIntervention']
#         intervention.save()



#         infrastructures = Infrastructures.objects.all()
#         serializer = InfrastructureSerializerDos(Interventions.objects.filter(Id_Infratrs__in=infrastructures), many=True)
        

#         return Response({'message':"les données pour planifier la date d'intervention sont recuent avec succè", 'data':InfrastructureSerializerDos.data}, status=201)


#     elif request.method == 'GET':
#         print()























# @api_view(['POST'])
# def create(request):
#     # Correction de request.body au lieu de request.boby
#     data = json.loads(request.body)
    
#     print(f'les data : ', data)
    
#     # Correction de la méthode objects
#     infrastructure = Infrastructures.objects.all()
    
#     # Utilisation correcte du serializer
#     serializer = InfractructureSerializer(infrastructure, many=True)

#     return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def hello_world(request):
    






























# from django.shortcuts import render

# # Create your views here.

# import json
# from django.shortcuts import render

# from django.http import JsonResponse
# from rest_framework import viewsets

# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
# from rest_framework import status 


# from AppGestionInfrastructure.models import Infrastructures, Interventions
# from AppGestionInfrastructure.serializers import AdministrationSerializer, CitoyenSerializer

# #Les ViewSets sont un moyen pratique de créer des endpoints 
# #pour les opérations CRUD (Create, Read, Update, Delete) sans beaucoup de code supplémentaire

# # class InfrastructuresViewSet(viewsets.ModelViewSet):
# #     queryset = Infrastructures.objects.all()
# #     serializer_class = InfrastructureSerializer 

# # class InterventionsViewSet(viewsets.ModelViewSet):
# #     queryset = Interventions.objects.all()
# #     serializer_class = InterventionsSerializer


# def inscriptionViewSet(vie):

#     def create(self, request, *arg, **kwarg):
#         if request.method == 'POST':
#         #     data = json.loads(request.body)
#         #     print(f'les datas du front : ', data)
#         #     return JsonResponse({'Message':'les donnes sont recu avec succès au niveau bakend'})
#         # else:
#             return JsonResponse({'Error': 'Invalid request method'}, status=405)




# class CitoyenViewSet(viewsets.ModelViewSet):
#     queryset = Infrastructures.objects.all()
#     serializer_class = CitoyenSerializer


#     #creation de la method liste pour retourner la liste des infrastructures et leurs date .°
#     def list(self, request, *args, **kwargs):
#         allInfrastructures = self.get_queryset()

#         #filtrons pour reccuperer le champ que nou souhaitons 

#         # firtre = []
#         # for index in allInfrastructures.data:
#         #     firtre.append({
#         #         'infratsNom': index['infratsNom'],
#         #         'infratsLocalition': index['infratsLocalition'],
#         #         'infratsDescrip': index['infratsDescrip'],
#         #         'infratsEtat': index['infratsEtat'],
#         #         'infratsDateEnrg': index['infratsDateEnrg'],
#         #         'intertnsDate': index['intervension']['intertnsDate'] if index.get('intervension') else None,

#         #     })
#         serializeAll = self.get_serializer(allInfrastructures,many=True)


#         return Response({"data": serializeAll}, status=status.HTTP_200_OK)




    
#     # créons une metho qui permet d'ajouter une infractructure  et retourner toute la liste de infractructure dans la base de donnée
#     def create (self, request, *arg, **kwargs ):
#         newInstance = self.get_serializer(data =request.data )
#         newInstance.is_valid(raise_exception=True)
#         infrastructures = newInstance.save()
#         AllListeInfractucture = Infrastructures.objects.all()
#         return  Response({"data": CitoyenSerializer(AllListeInfractucture, many=True).data, "message": "Infrastructure ajouter avec succès."}, status=status.HTTP_201_CREATED)
    

#     def update(self, request, pk=None, *args, **kwargs):
#             #recuperation de L'infractructure conncerner par les modification pour modifier
#         try:
#             infratrucSelect = self.object()
#             modif = self.get_serializer(infratrucSelect, data=request.data)

#             modif.is_valide(raise_exception=True)
#             modif.save()
#             AllListeInfractucture = Infrastructures.objects.all()
#             return Response({"data":CitoyenSerializer(AllListeInfractucture).data, "message": "infrastructure mise à jour avec succès."}, status=status.HTTP_200_OK)

#         except NotFound:
#             return Response({"message": "Infrastructure non trouvée."}, status=status.HTTP_404_NOT_FOUND)


# class AdministrationViewSet(viewsets.ModelViewSet):
#     queryset = Infrastructures.objects.all()
#     serializer_class = AdministrationSerializer







