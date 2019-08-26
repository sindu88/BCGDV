import json
import requests


# class GetAPI:
#     def __init__(self):
#         pass
#

url_base = "https://interns.bcgdvsydney.com"
req = requests.get(api_url_base + "/api/v1/key")
result = req.json()
print(req.json())
print(req.status_code)

key = result.get("key")
print(key)
contact = {"name": "Sinduja Sekar", "email": "sindhu.38@gmail.com"}
payload = {"apiKey": key}
req = requests.post(url_base + "/api/v1/submit", params=payload, data=json.dumps(contact))

print(req.json())

