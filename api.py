import requests

API_KEY = "a0592500b10be64c5c8aeadbc63e9faa"
BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {
    "x-apisports-key": API_KEY
}

def get_matchs_a_venir(league_id=61, season=2024, next_count=10):
    url = f"{BASE_URL}/fixtures"
    params = {
        "league": league_id,
        "season": season,
        "next": next_count
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()['response']
    else:
        print("Erreur (fixtures):", response.status_code, response.text)
        return []

def get_team_rank(team_id, league_id=61, season=2024):
    url = f"{BASE_URL}/standings"
    params = {
        "league": league_id,
        "season": season
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        standings = response.json()['response'][0]['league']['standings'][0]
        for team in standings:
            if team['team']['id'] == team_id:
                return team['rank']
    print("Erreur (rank):", response.status_code, response.text)
    return None

def get_team_form(team_id, league_id=61, season=2024):
    url = f"{BASE_URL}/teams/statistics"
    params = {
        "team": team_id,
        "league": league_id,
        "season": season
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        stats = response.json()['response']
        form_string = stats.get("form", "")
        # Calcule une forme simple : nombre de victoires sur les 5 derniers matchs
        return form_string.count("W")
    print("Erreur (form):", response.status_code, response.text)
    return 0