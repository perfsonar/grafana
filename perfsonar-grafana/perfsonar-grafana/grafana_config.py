#!/usr/bin/env python3

import configparser

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
    "org_name": "Main org.",
    "org_role": "Viewer"
}

#enable HTML in panels
grafana_ini['panels'] = {
     "disable_sanitize_html": 'true'
}

#write file
with open(GRAFANA_INI_FILE, 'w') as file:
        grafana_ini.write(file)