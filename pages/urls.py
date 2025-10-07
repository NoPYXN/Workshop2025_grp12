from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('joueurs.html>', views.joueurs, name='joueurs'),
    path('question1/<int:joueur_id>/', views.question1, name='question1'),
    path('documents.html', views.documents, name='documents'),

]