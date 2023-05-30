import requests

endpoint = "https://ronitlanguageresource-asayenuknufugpk.search.windows.net/synonymmaps/ronit-synonym-map?api-version=2021-04-30-Preview"
headers = {
        "Content-Type": "application/json",
        "api-key": "YpCu6FrWcwE8aIC5Qxb5lXIx1vbDlOEj6TtItHEKUzAzSeCEozOx"
    }

data = {
    "name": "ronit-synonym-map",
    "format": "solr",
    "synonyms": "United States, United States of America, USA, America, US\nNY, New York\nWashington, Wash., WA\nCalifornia, Calif., CA"
}

response = requests.put(endpoint, json=data, headers=headers, cookies={}, auth=())

print(response)
