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

# print(response)
################ LOGIN WITH NX-API REST ################
auth_url = "http:/192.168.2.12/api/mo/aaaLogin.json"
auth_body = {
    "aaaUser":{
        "attributes": {
            "name": switchuser,
            "pwd": switchpassword
        }
    }
}
auth_response = requests.post(url=auth_url,
                              data=json.dumps(auth_body),
                              timeout=5,
                              verify=False).json()
token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookies = {}
cookies["APIC-cookie"] = token
print(cookies)