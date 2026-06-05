import requests

username = "Wadan3"

response = requests.get(f"https://api.github.com/users/{username}")
data = response.json()

print(f"User: {data['login']}")
print(f"Followers: {data['followers']}")
print(f"Public repos: {data['public_repos']}")
