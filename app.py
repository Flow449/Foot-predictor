import streamlit as st
from api import get_matchs_a_venir, get_team_form, get_team_rank
from modeles import charger_modele, predire_resultat, predire_proba, predire_score

st.set_page_config(page_title="Prédictions Ligue 1", layout="wide")
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

        # Stats en temps réel
        home_rank = get_team_rank(home_id) or 10
        away_rank = get_team_rank(away_id) or 10
        home_form = get_team_form(home_id)
        away_form = get_team_form(away_id)

        # Prédictions IA
        resultat = predire_resultat(modele, home_rank, away_rank, home_form, away_form)
        proba = predire_proba(modele, home_rank, away_rank, home_form, away_form)
        home_score, away_score = predire_score(home_form, away_form)

        with st.container():
            st.subheader(f"{home_name} vs {away_name} – *{date}*")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**{home_name}**")
                st.write(f"Classement : {home_rank}")
                st.write(f"Forme : {home_form}/5")
            with col2:
                st.write(f"**{away_name}**")
                st.write(f"Classement : {away_rank}")
                st.write(f"Forme : {away_form}/5")

            st.success(f"Résultat prédit : **{resultat}**")
            st.info(f"Score estimé : {home_score} - {away_score}")

            st.markdown("**Probabilités :**")
            st.write(f"- Victoire {home_name} : {round(proba.get('H', 0)*100)}%")
            st.write(f"- Match nul : {round(proba.get('D', 0)*100)}%")
            st.write(f"- Victoire {away_name} : {round(proba.get('A', 0)*100)}%")

            st.markdown("---")
else:
    st.warning("Aucun match trouvé ou erreur avec l'API.")