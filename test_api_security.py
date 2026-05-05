import requests

headers = {"x-api-key": "supersecret882648"}
res = requests.get("http://127.0.0.1:5000/total-patients", headers=headers)
print(res.json())