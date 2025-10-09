import json
from pathlib import Path

class CulturalGuide:
    def __init__(self, data_path: str):
        data_file = Path(data_path)
        self.db = {m["id"]: m for m in json.loads(data_file.read_text(encoding="utf-8"))}

    def fiche(self, monument_id: str):
        m = self.db.get(monument_id)
        if not m:
            raise KeyError(monument_id)
        return {
            "titre": f"{m['nom']} ({m['pays']})",
            "resume": f"{m['nom']} se situe à {m['ville']}, en {m['pays']} ({m['continent']}).",
            "faits": m["faits"]
        }

    def candidates(self):
        return {mid: m["nom"] for mid, m in self.db.items()}
