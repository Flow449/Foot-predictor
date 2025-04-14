import requests

API_KEY = "a0592500b10be64c5c8aeadbc63e9faa"
API_URL = "https://v3.football.api-sports.io/fixtures"

headers = {
    "x-apisports-key": API_KEY
}

def get_matchs_a_venir(league_id=61, season=2024, next_count=10):
    params = {
        "league": league_id,  # Exemple : 61 = Ligue 1
        "season": season,
        "next": next_count
    }
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['response']
    else:
        print("Erreur:", response.status_code, response.text)
        return []