from ncclient import manager

router = {
    "host": "192.168.2.11",
    "port": "830",
    "username": "okan",
    "password": "hollander"
}

with manager.connect(host=router["host"],
                     port=router["port"],
                     username=router["username"],
                     password=router["password"],
                     hostkey_verify=False) as m:
    m.close_session()

