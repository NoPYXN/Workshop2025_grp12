from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, 'pages/accueil.html')

def joueurs(request):
    return render(request, 'pages/joueurs.html')

def j1(request):
    return render(request, 'pages/j1.html')

def j2(request):
    return render(request, 'pages/j2.html')

def j3(request):
    return render(request, 'pages/j3.html')

def documents(request):
    return render(request, 'pages/documents.html')
