import requests
import json
from tst import get_response


base_url = 'https://www.balldontlie.io/api/v1/'

def get_player():
    '''
    Gets information on the player chosen by the user.
    '''
    first_name = input("Enter the first name of the NBA player whose stats you want to see: ")
    last_name = input("Enter the last name of the NBA player whose stats you want to see: ")

    while first_name == "" or first_name.isdigit():
        first_name = input("Invalid input. Please try again: ")
    
    while last_name == "" or last_name.isdigit():
        last_name = input("Invalid input. Please try again: ") 
    return first_name.lower() + " " + last_name.lower()

# getting names and ids into one dict
def create_player_dict():
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

# Next to do, use input from user to search through dict <our_data> to find player id, make a new request to the api for stats, proceed from there
# Also, sort the dictionary by val


def main():
    print(get_player())
    print(create_player_dict())

if __name__ == "__main__":
    main()
