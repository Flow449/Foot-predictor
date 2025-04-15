import joblib
import os

def charger_modele():
    chemin = os.path.join("models", "modele.pkl")  # <- nom du bon dossier
    return joblib.load(chemin)
def predire_score(equipe_dom, equipe_ext, modele):
    # exemple fictif : retourne un score fixe
    return {
        "equipe_dom": equipe_dom,
        "equipe_ext": equipe_ext,
        "score_dom": 1,
        "score_ext": 2
    }
