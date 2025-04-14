import streamlit as st
from modeles import charger_modele, predire_resultat, predire_proba

# Chargement du modèle
modele = charger_modele()

st.title("Foot Predictor")
st.write("Entrez les données du match pour obtenir une prédiction :")

# Interface utilisateur
home_rank = st.number_input("Classement de l'équipe à domicile", min_value=1, max_value=20, value=10)
away_rank = st.number_input("Classement de l'équipe à l'extérieur", min_value=1, max_value=20, value=10)
home_form = st.slider("Forme de l'équipe à domicile (0 à 1)", 0.0, 1.0, 0.5)
away_form = st.slider("Forme de l'équipe à l'extérieur (0 à 1)", 0.0, 1.0, 0.5)

if st.button("Prédire le résultat"):
    resultat = predire_resultat(modele, home_rank, away_rank, home_form, away_form)
    proba = predire_proba(modele, home_rank, away_rank, home_form, away_form)

    st.subheader("Résultat prédit :")
    st.write(resultat)

    st.subheader("Probabilités :")
    for classe, p in proba.items():
        st.write(f"{classe} : {p:.2%}")