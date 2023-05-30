import requests

endpoint = "https://ronit-form-recognizer.cognitiveservices.azure.com/"
headers = {
        "Content-Type": "application/json",
        "api-key": "bef02779a0fe4725a3b5b23e17ec8a85"
    }

data = {
  "source": "https://ronitstorageaccount.blob.core.windows.net/ronit-container-2",
  "useLabelFile": True
}

response = requests.post(endpoint, json=data, headers=headers, cookies={}, auth=())

print(response)
print(response.text)
