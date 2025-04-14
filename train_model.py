import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Chargement du dataset
df = pd.read_csv("historique_matchs.csv")

# Préparation des données
X = df[["home_rank", "away_rank", "home_form", "away_form"]]
y = df["result"]

# Entraînement du modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Sauvegarde
joblib.dump(model, "modele_avance.pkl")
print("Modèle sauvegardé sous modele_avance.pkl")