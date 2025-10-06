from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, 'pages/accueil.html')

def joueurs(request):
    return render(request, 'joueurs.html')