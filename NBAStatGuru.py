import requests
import json
from backend import get_response, create_url, create_player_dict


base_url = 'https://www.balldontlie.io/api/v1/'


def get_player() -> str:
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


def find_player_id(player_name: str, our_data: dict) -> str:
    """
    Returns the player id for the desired player
    """
    while player_name not in our_data.keys():
        player_name = input("Sorry, player not found. Please enter a first and last name to try again: ").lower()
    return our_data[player_name]


def get_year() -> str:
    """
    Gets the input from the user if they want to specify a certain season
    """
    print("NOTE: The API only contains data from 1979-present")
    print("NOTE: The entered date implies the season from input year to the next")
    print("For example, an input of '2015' implies the 2015/2016 season")
    year = input("Enter a year in 'XXXX' format: ")
    while len(year) != 4 or int(year) < 1979 or int(year) > 2021:
        year = input("Please enter a valid year within the given parameters")
    return year


# Needs to be completed
def create_query(s) -> str:
    """
    Forms an appropriate query based on user specifications
    """
    pass


def run_program():
    print("Loading and updating necessary information...")
    our_data = create_player_dict()
    print("Done!")
    print()
    player_name = get_player()
    player_id = find_player_id(player_name, our_data)
    print(player_id)


def main():
    run_program()

if __name__ == "__main__":
    main()
