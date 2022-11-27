import requests
import json

url = "https://192.168.2.11:443/restconf/data/ietf-interfaces:interfaces"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback1337",
    "description": "added with restconf with Postman",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "137.137.137.137",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic b2thbjpob2xsYW5kZXI='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)