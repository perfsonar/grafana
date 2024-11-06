#!/usr/bin/env python3

import configparser
import random
import string
import json
import os

GRAFANA_INI_FILE='/etc/grafana/grafana.ini'
PSCONFIG_GRAFANA_FILE='/etc/perfsonar/psconfig/grafana-agent.json'

#read file
grafana_ini = configparser.ConfigParser()
try:
    grafana_ini.read(GRAFANA_INI_FILE)
except Exception:
    print('Duplicate section or option in', GRAFANA_INI_FILE)
    print('Trying to read it again without strict mode.')
    grafana_ini = configparser.ConfigParser(strict=False)
    grafana_ini.read(GRAFANA_INI_FILE)

#enable proxy
grafana_ini['server'] = {
    "root_url": '%(protocol)s://%(domain)s:%(http_port)s/grafana/'
}

#enable anonymous auth
grafana_ini['auth.anonymous'] = {
    "enabled": 'true',
    "org_name": "Main Org.",
    "org_role": "Viewer"
}

#enable HTML in panels
grafana_ini['panels'] = {
     "disable_sanitize_html": 'true'
}

#enable provisioning
grafana_ini['paths'] = {
    "provisioning": '/usr/lib/perfsonar/grafana/provisioning' 
}

# Set admin password if not set
if not (grafana_ini.has_section('security') and grafana_ini['security']):
    grafana_ini['security'] = {
        'admin_password': ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32)),
        'disable_initial_admin_creation': 'false'
    }

#write file
with open(GRAFANA_INI_FILE, 'w') as file:
        grafana_ini.write(file)

# Now configure psconfig
if os.path.exists(PSCONFIG_GRAFANA_FILE):
    with open(PSCONFIG_GRAFANA_FILE) as pgf_file_in:
        pgf_file_contents = json.loads(pgf_file_in.read())
    pgf_file_contents["grafana-user"] = "admin"
    pgf_file_contents["grafana-password"] = grafana_ini['security']['admin_password']
    with open(PSCONFIG_GRAFANA_FILE, "w") as pgf_file_out:
        pgf_file_out.write(json.dumps(pgf_file_contents, indent=4))
