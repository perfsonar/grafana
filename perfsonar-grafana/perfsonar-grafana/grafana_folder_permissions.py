#!/usr/bin/env python3

##
# This scripts sets the permissions on Grafana folders so that
# Viewers can View and Editors can Edit. Hopefully in future Grafana
# versions this won't be needed, but for now corrects issue where folders
# created as part of provisioning only allow Admin access.
#

import sys
import time
import configparser
import requests

GRAFANA_INI_FILE='/etc/grafana/grafana.ini'
GF_URL = "http://localhost:3000/api"
FOLDER_PERMISSIONS_JSON = {
  "items": [
    {
      "role": "Viewer",
      "permission": 1
    },
    {
      "role": "Editor",
      "permission": 2
    }
  ]
}

#parse command line args
folder_uids = sys.argv
folder_uids.pop(0)
if len(folder_uids) == 0:
    print("No uuids provided")
    sys.exit()

#read file
grafana_ini = configparser.ConfigParser()
grafana_ini.read(GRAFANA_INI_FILE)

#get admin password
admin_password = ''
if grafana_ini.has_option('security', 'admin_password'):
    admin_password = grafana_ini['security']['admin_password']
else:
    print("Unable to read admin password from {}".format(GRAFANA_INI_FILE))
    #no need to raise an error, just exit
    sys.exit()

#connect to api and update permissions
try_count = 0
TRY_MAX = 5
SLEEP_TIME=6
time.sleep(SLEEP_TIME)
while(try_count < TRY_MAX):
    try:
        for folder_uid in folder_uids:
            r = requests.post(
                    "{}/folders/{}/permissions".format(GF_URL,folder_uid), 
                    auth=('admin', admin_password),
                    headers={"Accept": "application/json","Content-Type": "application/json"},
                    json=FOLDER_PERMISSIONS_JSON,
                    verify=False,
                    timeout=12
                )
            r.raise_for_status()
        break
    except:
        print("Error talking to grafana, waiting")
        time.sleep(SLEEP_TIME)
    finally:
        try_count += 1
