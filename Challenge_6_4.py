import requests

endpoint = "https://ronitlanguageresource-asayenuknufugpk.search.windows.net/indexes/ronit-hotels-index/docs?" \
           "search=inn&scoringProfile=Geo&scoringParameter=CurrentLocation--122.123,44.77233&api-version=2021-04-30-Preview"
headers = {
        "Content-Type": "application/json",
        "api-key": "etIwAcLJ6rbfkv3UAffgPLH91b1iEwxKvPl6ZPv91HAzSeC20zTe"
    }

response = requests.get(endpoint, json={}, headers=headers, cookies={}, auth=())

print(response.text)
