import requests
import os

from dotenv import load_dotenv

load_dotenv()

GITHUB_ACCESS_TOKEN=os.getenv('GITHUB_PYTHON_SCRIPTING_ACCESS_TOKEN')
# Often, the 4 main HTTP request types will have to be performed on some data that is behind a user authentication wall
github_user_url = 'https://api.github.com/user'
github_user_url_response = requests.get(github_user_url)
# The following returns a json response that requires a user credentials
print(github_user_url_response.json())
# Can access the github api when using a personal token to access account data
github_user_url_response = requests.get(github_user_url, headers={'Authorization': f'token {GITHUB_ACCESS_TOKEN}'})
print(github_user_url_response.json())
