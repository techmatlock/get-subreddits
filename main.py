import os
import requests, requests.auth

CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')
USERNAME = os.environ.get('REDDIT_USERNAME')
PASSWORD = os.environ.get('REDDIT_PASSWORD')


def get_token():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": USERNAME, "password": PASSWORD}
    headers = {"User-Agent": "get-subreddits"}

    response = requests.post("https://www.reddit.com/api/v1/access_token", 
                             auth=client_auth, data=post_data, headers=headers)
    
    return response.json()["access_token"]

def get_subreddit_names(access_token): 
    headers = {"Authorization": f"bearer {access_token}", "User-Agent": "get-subreddits"}
    params = {"limit": 100}
    response = requests.get("https://oauth.reddit.com/subreddits/mine/subscriber", 
                            headers=headers, params=params)
    json_data = response.json()

    all_subreddit_names = []
    for subreddit_item in json_data["data"]["children"]:
        subreddit_name = subreddit_item["data"]["display_name"] 
        all_subreddit_names.append(subreddit_name)

    return all_subreddit_names

def main():
    access_token = get_token()

    get_subreddit_names(access_token)

if __name__ == "__main__":
    main()
