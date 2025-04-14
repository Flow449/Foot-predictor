import streamlit as st
from api import get_matchs_a_venir
from modeles import charger_modele, predire_resultat

st.set_page_config(page_title="Prédictions Ligue 1", layout="centered")
st.title("Prédictions Automatiques des Matchs de Ligue 1")

# Chargement du modèle
modele = charger_modele()

# Récupération des matchs
matchs = get_matchs_a_venir()

if matchs:
    for match in matchs:
        home = match['teams']['home']['name']
        away = match['teams']['away']['name']
        date = match['fixture']['date'].split("T")[0]

        # Variables fictives pour test (à remplacer par vraies stats API plus tard)
        home_rank = match['teams']['home'].get('ranking', 5)
        away_rank = match['teams']['away'].get('ranking', 8)
        home_form = 10  # placeholder
        away_form = 9   # placeholder

        resultat = predire_resultat(modele, home_rank, away_rank, home_form, away_form)

        st.markdown(f"**{home} vs {away}** — *{date}*")
        st.write(f"Prédiction : **{resultat}**")
        st.divider()
else:
    st.warning("Aucun match trouvé ou problème avec l'API.")