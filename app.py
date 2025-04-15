import streamlit as st
from modeles import charger_modele, predire_score

# Charger le modèle une fois
modele = charger_modele()

# Simuler les données de classement et forme (à remplacer par API ou CSV plus tard)
classement_dict = {
    "Paris SG": 1,
    "Marseille": 5,
    "Lyon": 10,
    "Nice": 3
}

forme_dict = {
    "Paris SG": 4,
    "Marseille": 2,
    "Lyon": 1,
    "Nice": 3
}

st.title("Prédiction de match de football")

# Sélection des équipes
equipe_dom = st.selectbox("Équipe à domicile", list(classement_dict.keys()))
equipe_ext = st.selectbox("Équipe à l'extérieur", list(classement_dict.keys()))

# Vérifier que les deux équipes sont différentes
if equipe_dom == equipe_ext:
    st.warning("Veuillez choisir deux équipes différentes.")
else:
    if st.button("Prédire le résultat"):
        resultat = predire_score(equipe_dom, equipe_ext, classement_dict, forme_dict, modele)
        
        if resultat["resultat"] == "home_win":
            st.success(f"{equipe_dom} devrait gagner.")
        elif resultat["resultat"] == "draw":
            st.info("Match nul prévu.")
        elif resultat["resultat"] == "away_win":
            st.success(f"{equipe_ext} devrait gagner.")
        else:
            st.error("Résultat inconnu.")
