# Get Subreddits

## Description
Python script to fetch all your subreddits you're subscribed to and convert them to a list.

## Demo

## Prerequisites
Requests==2.31.0

## Installation

1. Clone this repository to your local machine.
```
git clone https://github.com/techmatlock/get-subreddits.git
```
2. Create virtual environment ```python3 -m venv venv```
3. Install requirements ```pip3 install -r requirements.txt```
4. Export your environment variables to .bashrc (Linux) or .zshrc (Mac)
```
export REDDIT_CLIENT_ID="lkdfslafd9023lksd"
export REDDIT_CLIENT_SECRET="lldlsa_23l2k2l3kl233-th"
export REDDIT_USERNAME="username"
export REDDIT_PASSWORD="password"
```

## Configuration
1. Create your first developer app by going to https://www.reddit.com/prefs/apps
2. Give the app a name and once created, save your client id and client secret.
3. Go to https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
4. Used code snippets from Python example header.
5. I mostly used this API endpoint from the documentation - https://www.reddit.com/dev/api/#GET_subreddits_mine_subscriber

## Challenges/Obstacles Encountered
* I ran into an issue where the request object was a nested dictionary and couldn't be looped with a traditional for loop.  Each dictionary in json_data needed to be iterated and then from there I could extract the subreddit names from the json_data["data"] key.
* Another issue was the default limit of subreddits returned when making a GET request to /subreddits/mine/subscriber endpoint was it only returned 25 of my subreddits.  I had to add a parameter and set limit to the max 100 in the get_subreddit_names function.

## Errors

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.