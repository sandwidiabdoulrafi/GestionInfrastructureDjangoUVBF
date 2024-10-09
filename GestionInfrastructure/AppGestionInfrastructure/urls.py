from rest_framework.routers import DefaultRouter
from django.urls import path, include
# from AppGestionInfrastructure.view import CitoyenViewSet, AdministrationViewSet, inscriptionViewSet
from . import views

# router = DefaultRouter()
# router.register('citoyen', CitoyenViewSet, basename='citoyen')
# router.register('administration', AdministrationViewSet, basename='administration')
# router.register('inscription', inscriptionViewSet, basename='inscription')

urlpatterns = [

    path('sauveInfrastructureWithDateInterventions/', views.sauveInfrastructureWithDateInterventions, name='sauveInfrastructureWithDateInterventions' ),
    
    
    path('insertOneDataIntervention/', views.insertOneDataIntervention, name='insertOneDataIntervention'),

    path('InfrastructuresWithIntervensoinDate/', views.getAllInfrastructureWithIntevensionDate, name='InfrastructuresWithIntervensoinDate'),

    path('all-users/', views.allUserAdministration, name='all-users'),

    path('Login/', views.loginAdministration, name='Login'),

    path('SignUp/', views.SignUpAdministration, name='SignUp'),

    path('disconnection/', views.disconnection, name='disconnection'),

    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    
    path('CitizenSaveInfrastruct/', views.CitizenSaveInfrastruct, name='CitizenSaveInfrastruct'),

]











#----------------------aDMINISTRATION PERSONNELS------------


# loginAdministration
# SignUpAdministration
# allUserAdministration
# getAllInfrastructureWithIntevensionDate
# insertOneDataIntervention
# sauveInfrastructureWithDateInterventions




