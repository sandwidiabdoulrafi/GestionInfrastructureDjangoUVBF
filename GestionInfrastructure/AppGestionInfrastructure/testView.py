import requests






# #-------------------------inscription------------------

# endpoint = "http://127.0.0.1:8000/infratructure/SignUp/"
# inscriptionData= {'nom': 'sandwidi','prenom':'djaorata', 'tel':'+22664570512' , 'email':'djaorata@gmail.com','password':'djaorata'}
# response = requests.post(endpoint, json={'data': inscriptionData})

# print(response.json())
# print(response.status_code)


# try:
#     print("Response JSON:", response.json())
# except requests.exceptions.JSONDecodeError:
#     print("La réponse n'est pas un JSON valide.")



#-------------------------connexion------------------

# endpoint = "http://127.0.0.1:8000/infratructure/Login/"
# inscriptionData= {'email':'sandwidi@gmail.com','password':'123456'}
# response = requests.post(endpoint, json={'data':inscriptionData}) 

# print(response.json())
# print(response.status_code)


# try:
#     print("Response JSON:", response.json())
# except requests.exceptions.JSONDecodeError:
#     print("La réponse n'est pas un JSON valide.")




#________________renvoyer tout les utilisateur IL FAUT ETRE UNE personnne de l'administration___________________


# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/all-users/"

# # D'abord, connectez-vous pour créer une session

# endpointLogin = "http://127.0.0.1:8000/infratructure/Login/"

# login_data = {'email': 'sandwidi@gmail.com', 'password': '123456'}
# login_response = requests.post(endpointLogin, json={'data': login_data})

# # Vérifiez si la connexion a réussi
# if login_response.status_code == 201:

#     print("Connexion réussie")

#     print(login_response.json())

    
#     print("Response headers:", login_response.headers)
#     print("------------------------------",login_response.headers['Set-Cookie'],"--------", login_response.cookies,"-------------------------------------")
    
    
#     response = requests.post(endpoint, cookies=login_response.cookies)




#---------------------Insertion d'une infrastructure avec une date ------------


# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/sauveInfrastructureWithDateInterventions/"

# # D'abord, connectez-vous pour créer une session

# endpointLogin = "http://127.0.0.1:8000/infratructure/Login/"

# login_data = {'email': 'sandwidi@gmail.com', 'password': '123456'}
# login_response = requests.post(endpointLogin, json={'data': login_data})

# # Vérifiez si la connexion a réussi
# if login_response.status_code == 201:

#     print("Connexion réussie")

#     print(login_response.json())

    
#     print("Response headers:", login_response.headers)
#     print("------------------------------",login_response.headers['Set-Cookie'],"--------", login_response.cookies,"-------------------------------------")
    
#     inscriptionData= {'infrats': 'La nationnal Rn1','localisation':'Centre ville , Ouagadougou', 'desciprtion':'manque de voiture' , 'etat':'urgent','DateEnrg':'11/11/2024', 'dateIntervention':'2025-01-01'}
#     response = requests.post(endpoint,json={'data':inscriptionData}, cookies=login_response.cookies)

#     try:
#         print("Response JSON:", response.json())
        
#     except requests.exceptions.JSONDecodeError:
#         print("La réponse n'est pas un JSON valide.")



#---------------------recuperations des infrastructure et leurs dates d'intervension    je  vais configurer de sorte que sa ne soit pas que le personnel administration qui puisse le recperer le recuper-----------------------------


#version 1

# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/InfrastructuresWithIntervensoinDate/"

# # D'abord, connectez-vous pour créer une session

# endpointLogin = "http://127.0.0.1:8000/infratructure/Login/"

# login_data = {'email': 'sandwidi@gmail.com', 'password': '123456'}
# login_response = requests.post(endpointLogin, json={'data': login_data})

# # Vérifiez si la connexion a réussi
# if login_response.status_code == 201:

#     print("Connexion réussie")

#     response = requests.post(endpoint, cookies=login_response.cookies)

#     # print(response.json())
#     print(response.status_code)
#     print(response)

#     try:
#         print("Response JSON:", response.json())
        
#     except requests.exceptions.JSONDecodeError:
#         print("La réponse n'est pas un JSON valide.")



# #version 2


# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/InfrastructuresWithIntervensoinDate/"

# # D'abord, connectez-vous pour créer une session

# response = requests.post(endpoint)

# # print(response.json())
# print(response.status_code)
# print(response)

# try:
#     print("Response JSON:", response.json())
        
# except requests.exceptions.JSONDecodeError:
#     print("La réponse n'est pas un JSON valide.")








#-------------------------enregistrer seulement la date d'un infrastructure----------------------------

# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/insertOneDataIntervention/"

# # D'abord, connectez-vous pour créer une session

# endpointLogin = "http://127.0.0.1:8000/infratructure/Login/"

# login_data = {'email': 'sandwidi@gmail.com', 'password': '123456'}
# login_response = requests.post(endpointLogin, json={'data': login_data})

# # Vérifiez si la connexion a réussi
# if login_response.status_code == 201:

#     print("Connexion réussie")




#     Data= {'infrats': 'gendarmerie', 'dateIntervention':'2025-05-25'}
#     #json={'data':inscriptionData},
#     response = requests.post(endpoint,json={'data':Data}, cookies=login_response.cookies)

#     # print(response.json())
#     print(response.status_code)
#     print(response)

#     try:
#         print("Response JSON:", response.json())
        
#     except requests.exceptions.JSONDecodeError:
#         print("La réponse n'est pas un JSON valide.")





# #-------------------------Deconnexion-------------------------------------

# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/disconnection/"

# # D'abord, connectez-vous pour créer une session

# endpointLogin = "http://127.0.0.1:8000/infratructure/Login/"

# login_data = {'email': 'sandwidi@gmail.com', 'password': '123456'}
# login_response = requests.post(endpointLogin, json={'data': login_data})

# # Vérifiez si la connexion a réussi
# if login_response.status_code == 201:

#     print("Connexion réussie")


#     response = requests.post(endpoint, cookies=login_response.cookies)

#     # print(response.json())
#     print(response.status_code)
#     print(response)

#     try:
#         print("Response JSON:", response.json())
        
#     except requests.exceptions.JSONDecodeError:
#         print("La réponse n'est pas un JSON valide.")







# #-------------------------Suppression de compte-------------------------------------

# # L'endpoint pour obtenir tous les utilisateurs
# endpoint = "http://127.0.0.1:8000/infratructure/deleteAccount/"

# # D'abord, connectez-vous pour créer une session

# endpointLogin = "http://127.0.0.1:8000/infratructure/Login/"

# login_data = {'email': 'djaorata@gmail.com', 'password': 'djaorata'}
# login_response = requests.post(endpointLogin, json={'data': login_data})

# # Vérifiez si la connexion a réussi
# if login_response.status_code == 201:

#     print("Connexion réussie")

#     login_data = {'email': 'sandwidi@gmail.com', 'password': '123456'}

#     response = requests.post(endpoint, json={'data': login_data}, cookies=login_response.cookies)

#     # print(response.json())
#     print(response.status_code)
#     print(response)

#     try:
#         print("Response JSON:", response.json())
        
#     except requests.exceptions.JSONDecodeError:
#         print("La réponse n'est pas un JSON valide.")














#_-_-_-_-_-_-_-_-_-citoyen_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_



# # #-------------------------citoyen enregistrer un infrastructure-------------------------------------


# endpoint = "http://127.0.0.1:8000/infratructure/CitizenSaveInfrastruct/"






# inscriptionData= {'infrats': 'ecole public ','localisation':'Centre ville , Ouagadougou', 'desciprtion':'manque de voiture' , 'etat':'urgent','DateEnrg':'05/05/2024',}


# response = requests.post(endpoint, json={'data': inscriptionData})

# # print(response.json())
# print(response.status_code)
# print(response)

# try:
#     print("Response JSON:", response.json())
        
# except requests.exceptions.JSONDecodeError:
#     print("La réponse n'est pas un JSON valide.")







































# #--------------------------------------^^^^^^^^^^^^^^^^OK-----------------










# #-------------------------citoyen enregistrer un infrastructure-------------------------------------

# L'endpoint pour obtenir tous les utilisateurs
endpoint = "http://127.0.0.1:8000/infratructure/CitizenSaveInfrastruct/"

# D'abord, connectez-vous pour créer une session

inscriptionData= {'infrats': 'marche de dissiar','localisation':'Centre ville , Ouagadougou', 'desciprtion':'manque de voiture' , 'etat':'urgent','DateEnrg':'05/05/2024'}
#inscriptionData= {'infrats': 'police nationnal','localisation':'Centre ville , Ouagadougou', 'desciprtion':'manque de voiture' , 'etat':'urgent','DateEnrg':'06/02/2025'}


response = requests.post(endpoint, json={'data': inscriptionData})

# print(response.json())
print(response.status_code)
print(response)

try:
    print("Response JSON:", response.json())
        
except requests.exceptions.JSONDecodeError:
    print("La réponse n'est pas un JSON valide.")




































































