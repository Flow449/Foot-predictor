import streamlit as st
from api import get_matchs_a_venir, get_team_form, get_team_rank
from modeles import charger_modele, predire_resultat

st.set_page_config(page_title="Prédictions Ligue 1", layout="centered")
st.title("Prédictions Automatiques des Matchs de Ligue 1")

modele = charger_modele()
matchs = get_matchs_a_venir()

if matchs:
    for match in matchs:
        home_team = match['teams']['home']
        away_team = match['teams']['away']
        home_id = home_team['id']
        away_id = away_team['id']
        home_name = home_team['name']
        away_name = away_team['name']
        date = match['fixture']['date'].split("T")[0]

        # Récupération des vraies stats via API
        home_rank = get_team_rank(home_id) or 10
        away_rank = get_team_rank(away_id) or 10
        home_form = get_team_form(home_id)
        away_form = get_team_form(away_id)

        # Prédiction du résultat
        prediction = predire_resultat(modele, home_rank, away_rank, home_form, away_form)

        # Affichage
        st.markdown(f"### {home_name} vs {away_name} — *{date}*")
        st.write(f"Classement : {home_name} ({home_rank}) vs {away_name} ({away_rank})")
        st.write(f"Forme actuelle : {home_form}W - {away_form}W (sur 5 derniers matchs)")
        st.success(f"**Prédiction IA** : {prediction}")
        st.divider()
else:
    st.warning("Aucun match trouvé ou erreur API.")