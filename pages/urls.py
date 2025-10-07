from django.urls import path
from . import views

urlpatterns = [
    #path('', views.accueil, name='accueil'),
    path('joueurs/', views.joueurs, name='joueurs'),
    path('j1.html', views.j1, name='j1'),
    path('j2.html', views.j2, name='j2'),
    path('j3.html', views.j3, name='j3'),
    
]