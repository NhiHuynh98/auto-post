import json
import requests
import schedule
import time

# APP_ID: 616779434494890
# APP_SECRET: 4482a841f3865f556d180fd52c752b3f

# Replace with your access token and page/group ID
ACCESS_TOKEN = "EAAOZBR7rMs98BO86eo9QOvcTNZCOjXzbr3PGg6GnmYcCYQ6IEuIRiMIE6uS9K1efdkNQgbtC7i6RKcDPUveQXgJZAYyiSNMpUXim4ZAEV8eI0RYvpcro6cdwHeA05FZB1aZBlz6I3UkbPhWKYXvOKJ3ISwjuVmo7tUyGPzNKfFIBH8R7IHCVyVJgz79c9qE78FFY3UdTEQJf1kgMof4jWtRX520eQZD"
PAGE_ID = "939469823513712"
MESSAGE = "🚀 Automated News Update: Your latest news content here!"

def post_to_facebook_group():
    url = f"https://wwww.facebook.com/groups/{PAGE_ID}"
    payload = {
        "message": MESSAGE,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)

    try:
        if response.status_code == 200:
            print("Post successfully published!")
            # Save response to a file
            with open("facebook_post_response.txt", "w", encoding="utf-8") as file:
                file.write(response.text)
        else:
            print("Failed to post:", response)
    except json.JSONDecodeError:
        print("Error: Response is not in JSON format.")

def post_to_facebook():
    post_url = f'https://graph.facebook.com/v18.0/{PAGE_ID}/feed'
    response = requests.post(post_url, params={'access_token': ACCESS_TOKEN, 'message': MESSAGE})

    if response.status_code == 200:
        print("Post successfully created!")
    else:
        print(f"Error creating post. Status code: {response.status_code}")
        print(response.json())  # Print the error details

post_to_facebook()


# curl -i -X GET \
#   "https://graph.facebook.com/1249148589742745?fields=id,name,email,picture&access_token=EAAOZBR7rMs98BO86eo9QOvcTNZCOjXzbr3PGg6GnmYcCYQ6IEuIRiMIE6uS9K1efdkNQgbtC7i6RKcDPUveQXgJZAYyiSNMpUXim4ZAEV8eI0RYvpcro6cdwHeA05FZB1aZBlz6I3UkbPhWKYXvOKJ3ISwjuVmo7tUyGPzNKfFIBH8R7IHCVyVJgz79c9qE78FFY3UdTEQJf1kgMof4jWtRX520eQZD"


# curl -i - X POST "https://graph.facebook.com/52056223/feed?message=Hello&fields=created_time,from,id,message&access_token=EAAOZBR7rMs98BO86eo9QOvcTNZCOjXzbr3PGg6GnmYcCYQ6IEuIRiMIE6uS9K1efdkNQgbtC7i6RKcDPUveQXgJZAYyiSNMpUXim4ZAEV8eI0RYvpcro6cdwHeA05FZB1aZBlz6I3UkbPhWKYXvOKJ3ISwjuVmo7tUyGPzNKfFIBH8R7IHCVyVJgz79c9qE78FFY3UdTEQJf1kgMof4jWtRX520eQZD"

# Check page can be access
# curl -X GET "https://graph.facebook.com/v19.0/me/groups?access_token=EAAOZBR7rMs98BOz2e2jnMEi16f4iPEWfJZAchR5MavXpJFsxvvISmIYuhvxLQ7ZAINp7lZCAGEZATnUgTuiUbucxYllvZBRrwMuMFcQ4dfDm7s4WIdqblCirPYfZCP1kgIImO6WzVRGEAKdhZCqLSapkCiKOBKlYNvyz4Ndey2PAKUtniwY3Trr4cJvSGIDUxHptiXYvaBDlXX9nzOZAZBlxytt8ZBqME8ZD"









# post_to_facebook_group()

# curl -X POST "https://wwww.facebook.com/groups/939469823513712" \
#      -d "message=Hello, this is a test post from cURL!" \
#      -d "access_token=EAAOZBR7rMs98BO1qrDG2JQDuAGZBvzgFYywrdDRlNzhsZB6e2ategNl5s7zXW5zJ5CL6R61CdPpyzwv4v7b2ZBRzR0me8IPBnGCl59zSDDZB7V0uPfr3W46H9ZBhustb268MoSjsoVV6WmmQ8VmJ7ygewo7yZBMtLZAbopgZAP5E4K9RG3LZCrkIXEZAZB48PI5pAmmFiZBsPYlYJKN6RwmDpmHRi7D0BmuMY"


# def fetch_recent_posts():
#     url = f"https://wwww.facebook.com/groups/${PAGE_ID}?access_token={ACCESS_TOKEN}"
#     response = requests.get(url)
#     with open("facebook_get_response.txt", "w", encoding="utf-8") as file:
#                 file.write(response.text)
    
#     print("Response Status Code:", response.status_code)
#     print("Raw Response Text:", response)

# fetch_recent_posts()
# curl -X GET "https://wwww.facebook.com/groups/939469823513712?access_token=EAAOZBR7rMs98BO1qrDG2JQDuAGZBvzgFYywrdDRlNzhsZB6e2ategNl5s7zXW5zJ5CL6R61CdPpyzwv4v7b2ZBRzR0me8IPBnGCl59zSDDZB7V0uPfr3W46H9ZBhustb268MoSjsoVV6WmmQ8VmJ7ygewo7yZBMtLZAbopgZAP5E4K9RG3LZCrkIXEZAZB48PI5pAmmFiZBsPYlYJKN6RwmDpmHRi7D0BmuMY"
# 
# Schedule to post every day at 9 AM
# schedule.every().day.at("09:00").do(post_to_facebook)
# while True:
#     schedule.run_pending()
#     time.sleep(60)
