import joblib

def charger_modele():
    return joblib.load("modele.pkl")

def predire_resultat(modele, home_team, away_team, home_goals, away_goals):
    features = [[home_goals, away_goals]]
    prediction = modele.predict(features)
    return prediction[0]
