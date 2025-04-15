# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Chargement des données
df = pd.read_csv("historique_matchs.csv")

# Vérification des colonnes attendues
features = ["home_rank", "away_rank", "home_form", "away_form"]
target = "result"

if not all(col in df.columns for col in features + [target]):
    raise ValueError(f"Les colonnes attendues sont manquantes. Il faut : {features + [target]}")

X = df[features]
y = df[target]

# Entraînement du modèle
model = RandomForestClassifier()
model.fit(X, y)

# Création du dossier 'models' s'il n'existe pas
os.makedirs("models", exist_ok=True)

# Sauvegarde du modèle
joblib.dump(model, "models/modele_rf.joblib")

print("Modèle entraîné et sauvegardé dans models/modele_rf.joblib")
