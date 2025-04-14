import streamlit as st
from modeles import charger_modele, predire_resultat

st.title("Prédiction de Matchs de Football")
st.write("Entrez les statistiques pour obtenir une prédiction.")

home_team = st.text_input("Équipe à domicile")
away_team = st.text_input("Équipe à l'extérieur")
home_goals = st.number_input("Buts domicile", min_value=0, step=1)
away_goals = st.number_input("Buts extérieur", min_value=0, step=1)

if st.button("Prédire"):
    modele = charger_modele()
    prediction = predire_resultat(modele, home_team, away_team, home_goals, away_goals)
    st.success(f"Résultat prédit : {prediction}")
