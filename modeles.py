import joblib
import pandas as pd

def charger_modele(path='modele_avance.pkl'):
    return joblib.load(path)

def preparer_features(home_rank, away_rank, home_form, away_form):
    return pd.DataFrame([{
        "home_rank": home_rank,
        "away_rank": away_rank,
        "home_form": home_form,
        "away_form": away_form
    }])

def predire_resultat(modele, home_rank, away_rank, home_form, away_form):
    features = preparer_features(home_rank, away_rank, home_form, away_form)
    prediction = modele.predict(features)
    return prediction[0]

def predire_proba(modele, home_rank, away_rank, home_form, away_form):
    features = preparer_features(home_rank, away_rank, home_form, away_form)
    proba = modele.predict_proba(features)[0]
    classes = modele.classes_
    return dict(zip(classes, proba))

def predire_score(home_form, away_form):
    # Estimation simple du score basé sur la forme
    home_goals = round(1 + (home_form * 0.3))
    away_goals = round(1 + (away_form * 0.3))
    return min(home_goals, 5), min(away_goals, 5)