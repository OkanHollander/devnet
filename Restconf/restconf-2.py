import requests
import json

url = "https://192.168.2.11:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic b2thbjpob2xsYW5kZXI='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

api_data = response.json()
print("*"*50)
print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("*"*50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
  print("Interface is up")