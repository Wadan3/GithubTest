import requests

username = "Wadan3"

response = requests.get(
    f"https://api.github.com/users/{username}"
)

data = response.json()

print("Name:", data.get("name"))
print("Username:", data.get("login"))
print("Public Repos:", data.get("public_repos"))
print("Followers:", data.get("followers"))
