import requests
import json

target = "http://192.168.2.13/ins"
username = "admin"
password = "admin"

request_headers = {
    "Content-Type": "application/json"
}
show_cmd = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show ip int brief",
        "output_format": "json"
    }
}

response = requests.post(
    target,
    data=json.dumps(show_cmd),
    headers=request_headers,
    auth=(username, password),
    verify=False
).json()

print(json.dumps(response, indent=2, sort_keys=True))