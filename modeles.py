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