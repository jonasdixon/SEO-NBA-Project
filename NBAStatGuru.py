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
    url = "https://www.balldontlie.io/api/v1/players"
    big_dict = get_response(url) # this is only returning the players and ids from the "first page" of the json output
    data_list = big_dict["data"]
    our_data = {}
    for i in range(len(data_list)):
        player_id = data_list[i]["id"]
        player_first_name = data_list[i]["first_name"].lower()
        player_last_name = data_list[i]["last_name"].lower()
        our_data[player_id] = player_first_name + " " + player_last_name
    return our_data




def main():
    print(get_player())
    print(create_player_dict())

if __name__ == "__main__":
    main()
