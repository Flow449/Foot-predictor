import joblib
import numpy as np

def charger_modele():
    chemin = "modeles/modele_rf.joblib"
    return joblib.load(chemin)

def predire_resultat(modele, home_rank, away_rank, home_form, away_form):
    features = [[home_rank, away_rank, home_form, away_form]]
    prediction = modele.predict(features)[0]
    return prediction

def predire_proba(modele, home_rank, away_rank, home_form, away_form):
    features = [[home_rank, away_rank, home_form, away_form]]
    proba = modele.predict_proba(features)[0]
    classes = modele.classes_
    return dict(zip(classes, proba))

def predire_score(home_form, away_form):
    home_score = np.clip(int(home_form / 1.5), 0, 4)
    away_score = np.clip(int(away_form / 1.5), 0, 4)
    return home_score, away_score