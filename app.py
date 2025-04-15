import streamlit as st
from modeles import charger_modele, predire_score

st.title("Prédicteur de Matchs de Football")

# Entrée utilisateur
home_rank = st.slider("Classement de l'équipe à domicile", 1, 20, 10)
away_rank = st.slider("Classement de l'équipe à l'extérieur", 1, 20, 10)
home_form = st.slider("Forme de l'équipe à domicile (sur 5)", 0, 5, 3)
away_form = st.slider("Forme de l'équipe à l'extérieur (sur 5)", 0, 5, 3)

if st.button("Prédire le résultat"):
    modele = charger_modele()
    prediction = predire_resultat(modele, home_rank, away_rank, home_form, away_form)
    proba = predire_proba(modele, home_rank, away_rank, home_form, away_form)

    st.subheader("Résultat prédit :")
    st.write(prediction)

    st.subheader("Probabilités :")
    st.write(proba)
