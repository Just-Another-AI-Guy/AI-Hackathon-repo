import requests

endpoint = "https://ronitlanguageresource-asayenuknufugpk.search.windows.net/indexes/hotels-index-unenriched/docs/search?api-version=2021-04-30-Preview"
headers = {
        "Content-Type": "application/json",
        "api-key": "etIwAcLJ6rbfkv3UAffgPLH91b1iEwxKvPl6ZPv91HAzSeC20zTe"
    }

data1 = {
    "search": "*",
    "queryType": "simple",
    "select": "HotelName, Category",
    "count": True
}

data2 = {
    "search": "HotelName:(hotel NOT motel) AND Category:'Resort and Spa'",
    "queryType": "full",
    "select": "HotelId, HotelName, Category, Tags, Description",
    "count": True
}

response_simple = requests.post(endpoint, json=data1, headers=headers, cookies={}, auth=())
response_full = requests.post(endpoint, json=data2, headers=headers, cookies={}, auth=())

print(response_simple.text)
print("\n")
print(response_full.text)
