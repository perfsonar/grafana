#!/bin/bash

PS_ROOT="/usr/lib/perfsonar/grafana"
PS_IMG_ROOT="${PS_ROOT}/images"
GF_IMG_DIR="/usr/share/grafana/public/img/"

#Update grafana.ini
${PS_ROOT}/grafana_config.py

#Install custom images
mv -f ${PS_IMG_ROOT}/*.svg ${GF_IMG_DIR}/

#Restart grafana
systemctl restart grafana-server.service
