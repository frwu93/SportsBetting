import nba_api_client
import pandas as pd


# Get teams data from API
api_client = nba_api_client.NbaApiClient()
teams = api_client.get_nba_teams()
nba_teams = [team for team in teams if team["nbaFranchise"] == True and team["allStar"] == False]

nba_teams_df = pd.json_normalize(nba_teams, sep='_')
clean_nba_teams_df = nba_teams_df.drop(columns=["allStar", "nbaFranchise"])
clean_nba_teams_df = clean_nba_teams_df.rename(columns={"id": "teamId", "leagues_standard_conference": "conference", "leagues_standard_division": "division"})
clean_nba_teams_df.to_csv("saved_data/nba_teams.csv", index=False)