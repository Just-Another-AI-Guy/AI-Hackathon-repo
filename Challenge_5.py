import requests

endpoint = "https://ronitlanguageresource-asayenuknufugpk.search.windows.net/indexes/ronit-hotels-index/docs/search?api-version=2021-04-30-Preview"
headers = {
        "Content-Type": "application/json",
        "api-key": "etIwAcLJ6rbfkv3UAffgPLH91b1iEwxKvPl6ZPv91HAzSeC20zTe"
    }

data = {
    "search": "document/content/*",
    "select": "TopTen",
}

response = requests.post(endpoint, json=data, headers=headers, cookies={}, auth=())

print(response.text)
