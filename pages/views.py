from django.shortcuts import render

def accueil(request):
    return render(request, 'pages/accueil.html')

def joueurs(request):
    return render(request, 'pages/joueurs.html')

def question1(request, joueur_id):
    return render(request, 'pages/Question1.html', {'joueur_id': joueur_id})
