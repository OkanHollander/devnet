from dnacentersdk import api
import json
import time
import calendar

dna = api.DNACenterAPI(base_url="https://sandboxdna2.cisco.com",
                       username="devnetuser", password="Cisco123!")


###### Network and Sites ######

# Print Site Topology
