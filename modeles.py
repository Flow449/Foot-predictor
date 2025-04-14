import pickle
import numpy as np

def charger_modele(path="models/modele.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def predire_resultat(modele, home_rank, away_rank, home_form, away_form):
    features = [[home_rank, away_rank, home_form, away_form]]
    prediction = modele.predict(features)[0]
    if prediction == 'H':
        return "Victoire domicile"
    elif prediction == 'A':
        return "Victoire extérieur"
    else:
        return "Match nul"

def predire_proba(modele, home_rank, away_rank, home_form, away_form):
    features = [[home_rank, away_rank, home_form, away_form]]
    proba = modele.predict_proba(features)[0]
    return {"H": proba[0], "D": proba[1], "A": proba[2]}

def predire_score(home_form, away_form):
    home_score = np.clip(int(home_form / 1.5), 0, 4)
    away_score = np.clip(int(away_form / 1.5), 0, 4)
    return home_score, away_score