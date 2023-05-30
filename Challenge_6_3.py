import requests

endpoint = "https://ronitlanguageresource-asayenuknufugpk.search.windows.net/indexes/ronit-hotels-index/docs/autocomplete?api-version=2021-04-30-Preview"
headers = {
        "Content-Type": "application/json",
        "api-key": "YpCu6FrWcwE8aIC5Qxb5lXIx1vbDlOEj6TtItHEKUzAzSeCEozOx"
    }

data = {
  "autocompleteMode": "oneTerm",
  "search": "Wash",
  "suggesterName": "Ronit",
}

response = requests.post(endpoint, json=data, headers=headers, cookies={}, auth=())

print(response.text)
