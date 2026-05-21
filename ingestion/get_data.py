import requests
import json

def fetch():
    url = "https://api.github.com/users/torvalds/repos"
    response = requests.get(url)
    return response.jsogn()

def save_to_file(data):
    with open("data/data.json", "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    data = fetch()
    save_to_file(data)