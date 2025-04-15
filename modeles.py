import joblib
import os

def charger_modele():
    chemin = os.path.join("models", "modele.pkl")  # <- nom du bon dossier
    return joblib.load(chemin)
