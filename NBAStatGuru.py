import requests
import json

base_url = 'https://www.balldontlie.io/api/v1/'

def get_player():
    '''
    Gets information on the player chosen by the user.
    '''
    first_name = input("Enter the first name of the NBA player whose stats you want to see: ")
    last_name = input("Enter the last name of the NBA player whose stats you want to see: ")

    while first_name == "" or first_name.isdigit():
        first_name = input("Invalid input. Please try again: ")
    
    while last_name.isdigit():
        last_name = input("Invalid input. Please try again: ") 
    return first_name.lower() + " " + last_name.lower()

def main():
    print(get_player())

if __name__ == "__main__":
    main()

# while specify not in cases.keys():
#     raise IndexError("That key was not valid to give any data from the API")
# return base_url + cases[specify]