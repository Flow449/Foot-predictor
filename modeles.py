
import joblib
import os

def charger_modele():
    chemin = os.path.join("modeles", "modele.pkl")
    return joblib.load(chemin)
