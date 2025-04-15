import joblib
import os

def charger_modele():
    chemin = os.path.join("models", "modele.pkl")
    return joblib.load(chemin)