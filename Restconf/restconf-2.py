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