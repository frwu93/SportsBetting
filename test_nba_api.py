import utils
import requests

"""
Run this file to test your NBA API token.
"""

nba_api_key = utils.get_api_key("NBA_API_KEY")


url = "https://api-nba-v1.p.rapidapi.com/games/statistics"

querystring = {"id":"10403"}

headers = {
	"x-rapidapi-key": nba_api_key,
	"x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())