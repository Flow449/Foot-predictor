import requests

API_KEY = "a0592500b10be64c5c8aeadbc63e9faa"
BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_matchs_a_venir(league_id=61, season=2024):
    url = f"{BASE_URL}/fixtures?league={league_id}&season={season}&next=10"
    try:
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        return data.get("response", [])
    except:
        return []

def get_team_form(team_id):
    url = f"{BASE_URL}/teams/statistics?team={team_id}&season=2024&league=61"
    try:
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        form = data["response"]["form"]
        return form.count('W')
    except:
        return 2

def get_team_rank(team_id):
    url = f"{BASE_URL}/standings?season=2024&league=61"
    try:
        response = requests.get(url, headers=HEADERS)
        standings = response.json()["response"][0]["league"]["standings"][0]
        for team in standings:
            if team["team"]["id"] == team_id:
                return team["rank"]
    except:
        return None