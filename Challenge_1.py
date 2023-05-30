import requests

endpoint = "https://ronit-language-resource.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=Ronit-QA-Knowledge-Base&api-version=2021-10-01&deploymentName=production"
headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "41ee94bb9121445893c55884210782aa"
    }

data = {"top": 3, "question": "How do I install Jenkins?", "includeUnstructuredSources": True, "confidenceScoreThreshold": "0.8"}

response = requests.post(endpoint, json=data, headers=headers, cookies={}, auth=())

print(response.text)
