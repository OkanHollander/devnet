from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

api_token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
meraki = MerakiSdkClient(api_token)

orgs = meraki.organizations.get_organizations()
# pprint(orgs)
for org in orgs:
    if org["name"] == "DevNetAssoc":
        orgID = org["id"]
        
# print(orgID)

params = {}
params["organization_id"] = orgID
networks = meraki.networks.get_organization_networks(params)
# pprint(networks)
for network in networks:
    if network["name"] == "DevNetAssoc3":
        netID = network["id"]
vlans = meraki.vlans.get_network_vlans(netID)
# print(vlans)