from django.shortcuts import render

def accueil(request):
    return render(request, 'pages/accueil.html')

def joueurs(request):
    return render(request, 'pages/joueurs.html')

def documents(request):
    return render(request, 'pages/documents.html')