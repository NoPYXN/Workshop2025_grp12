from django.http import JsonResponse
from .guide import CulturalGuide

DATA_PATH = "ai/data/monuments.json"
guide = CulturalGuide(DATA_PATH)

def health(request):
    return JsonResponse({"status": "ok"})

def fiche(request, monument_id):
    try:
        return JsonResponse(guide.fiche(monument_id))
    except KeyError:
        return JsonResponse({"error": "monument inconnu"}, status=404)
