import requests
from requests.adapters import HTTPAdapter, Retry
import utils
import json

class NbaApiClient:
    BASE_URL = "https://api-nba-v1.p.rapidapi.com"
    NBA_API_KEY = utils.get_api_key("NBA_API_KEY")
    HEADERS ={
	    "x-rapidapi-key": NBA_API_KEY,
	    "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
    }


    def __init__(self):
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def get_nba_teams(self):
        """Fetch NBA player stats from the API."""
        url = f"{self.BASE_URL}/teams?league=standard"        
        response = self.session.get(url, headers=self.HEADERS)
        response.raise_for_status()
        data = response.json()
        return data["response"]
