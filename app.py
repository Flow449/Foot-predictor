import streamlit as st
from api import get_matchs_a_venir, get_team_form, get_team_rank
from modeles import charger_modele, predire_resultat

st.set_page_config(page_title="Prédictions Ligue 1 - Détail", layout="wide")
st.title("Prédictions détaillées des matchs de Ligue 1")

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

        # Récupération des stats en live
        home_rank = get_team_rank(home_id) or 10
        away_rank = get_team_rank(away_id) or 10
        home_form = get_team_form(home_id)
        away_form = get_team_form(away_id)

        # Prédiction avec le modèle IA
        prediction = predire_resultat(modele, home_rank, away_rank, home_form, away_form)

        # Affichage détaillé
        with st.container():
            st.subheader(f"{home_name} vs {away_name} – {date}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{home_name}**")
                st.write(f"- Classement : {home_rank}")
                st.write(f"- Forme : {home_form}/5 (Victoires)")
            with col2:
                st.markdown(f"**{away_name}**")
                st.write(f"- Classement : {away_rank}")
                st.write(f"- Forme : {away_form}/5 (Victoires)")

            st.success(f"**Prédiction IA** : {prediction}")
            st.markdown("---")
else:
    st.warning("Aucun match trouvé ou erreur avec l'API.")