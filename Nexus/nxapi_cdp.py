import requests
import json

switchuser= "cisco"
switchpassword = "cisco"

url = "http:/192.168.2.12/ins"
headers = {"content-type": "application/json"}
payload = {
    "ins_api" : {
        "version": "1.0",
        "type": "cli_show",
        "chuck": "0",
        "sid": "1",
        "input": "show cdp neighbor",
        "output_format": "json"
    }
}

response = requests.post(url=url, 
                         data=json.dumps(payload), 
                         headers=headers, 
                         auth=(switchuser, switchpassword), 
                         verify=False).json()

print(response)