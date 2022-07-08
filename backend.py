import requests
import json


def create_url() -> str:
    """
    Design the url to access the season_averages endpoint of the API
    """
    base_url = 'https://www.balldontlie.io/api/v1/'
    return base_url + 'season_averages'


def get_response(url) -> dict:
    """
    Making the request to the API and returning data as a parsed json file
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()


def create_player_dict() -> dict:
    """
    Creating a dictionary of all the players in the API
    """
    url = "https://www.balldontlie.io/api/v1/players?per_page=100"

    our_data = {}
    
    for i in range(1, 39):
        
        colect_dict = get_response(url+"&page={}".format(i))
        data_lists = colect_dict["data"]
        
        for j in range(len(data_lists)):
        
            player_id = data_lists[j]["id"]
            player_first_name = data_lists[j]["first_name"].lower()
            player_last_name = data_lists[j]["last_name"].lower()
            full_name = player_first_name + " " + player_last_name
            our_data[full_name] = str(player_id)
    
    return our_data