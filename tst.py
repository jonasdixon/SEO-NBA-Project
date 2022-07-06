import requests
import json

#url = 'https://www.balldontlie.io/api/v1/'

#print("Input an option below to navigate the BallDontLie API: ")
#specify = input("\n 1 - players \n 2 - teams \n 3 - games \n 4 - stats \n 5 - season_stats\n ")

def create_url():
    """
    Design the url to access the API based on the parameters set by the user
    """

    base_url = 'https://www.balldontlie.io/api/v1/'

    print("Input an option (input only the number) below to navigate the BallDontLie API: ")
    # specify has type <str>
    specify = input("\n 1 - players \n 2 - teams \n 3 - games \n 4 - stats \n 5 - season_averages\n ")
    cases = {
            "1": "players",
            "2": "teams",
            "3": "games",
            "4": "stats",
            "5": "season_averages"
            }
# add a try except block here
    while: specify not in cases.keys():
        raise IndexError("That key was not valid to give any data from the API")
    return base_url + cases[specify]


def get_response(url):
    """
    Making the request to the API and returning data as a parsed json file
    """
    response = requests.get(url)
    print(response.status_code)
    if response.status_code!=200:
        raise Exception("Request returned an error: {} {}".format(
                res.status_code, res.text
            )
        )

    return response.json()


if __name__=='__main__':
    # first step of building the url and accessing the information
    r = create_url()
    # this is the dictionary of all the data
    formatted = get_response(r)
    # formatted = response.json()

    # This line is returning cryptic error code, look into it further
    # json.dumps(get_response(formatted), indent=4, sort_keys=True)

    print(formatted)
    