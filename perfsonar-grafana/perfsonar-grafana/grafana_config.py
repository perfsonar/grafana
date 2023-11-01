#!/usr/bin/env python3

import configparser
import random
import string

GRAFANA_INI_FILE='/etc/grafana/grafana.ini'

#read file
grafana_ini = configparser.ConfigParser()
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
        'disable_initial_admin_creation': 'true'
    }

#write file
with open(GRAFANA_INI_FILE, 'w') as file:
        grafana_ini.write(file)