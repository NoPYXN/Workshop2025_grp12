from django.shortcuts import render

def accueil(request):
    return render(request, 'pages/accueil.html')

def joueurs(request):
    return render(request, 'pages/joueurs.html')

def documents(request):
    return render(request, 'pages/documents.html')

def question1(request, joueur_id):
    return render(request, 'pages/question1.html', {'joueur_id': joueur_id})

def question2(request, joueur_id):
    return render(request, 'pages/question2.html', {'joueur_id': joueur_id})

def question3(request, joueur_id):
    return render(request, 'pages/question3.html', {'joueur_id': joueur_id})