import joblib

def charger_modele():
    chemin = "models/modele.joblib"  # chemin vers le modèle dans le dossier models
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
