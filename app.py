import streamlit as st
from api import get_matchs_a_venir

st.set_page_config(page_title="Prédiction Football", layout="centered")
st.title("Matchs à venir - Ligue 1")

# Affichage des prochains matchs
matchs = get_matchs_a_venir()

if matchs:
    for match in matchs:
        home = match['teams']['home']['name']
        away = match['teams']['away']['name']
        date = match['fixture']['date'].split("T")[0]
        st.markdown(f"**{home}** vs **{away}** — *{date}*")
else:
    st.warning("Aucun match trouvé ou problème avec l'API.")