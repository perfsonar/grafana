#!/bin/bash

#include shared vars
. $(dirname $0)/grafana_common.sh

PS_ROOT="/usr/lib/perfsonar/grafana"
PS_IMG_ROOT="${PS_ROOT}/images"
PS_PLUGIN_ROOT="${PS_ROOT}/plugins"
GF_IMG_DIR="/usr/share/grafana/public/img/"
GF_PLUGIN_DIR="/var/lib/grafana/plugins/"

#Update grafana.ini
grep -q "Grafana Configuration Example" /etc/grafana/grafana.ini
if [ $? == 0 ]; then
    cp -f /etc/grafana/grafana.ini /etc/grafana/grafana.ini.example
fi
${PS_ROOT}/grafana_config.py

#Make an empty directory used by provisioning to create empty folders
mkdir -p ${PS_ROOT}/dashboards/empty

#Install custom images
mv -f ${PS_IMG_ROOT}/*.svg ${GF_IMG_DIR}/

####
# Install plugins
mkdir -p ${GF_PLUGIN_DIR}

# remove old plugins
for prm in "${PLUGINS_TO_REMOVE[@]}"
do
: 
   rm -rf ${GF_PLUGIN_DIR}/${prm}
done

# install new plugins
cd ${PS_PLUGIN_ROOT}
for plugin_name in "${!PLUGINS_TO_INSTALL[@]}"
do
: 
   unzip -q -d ${GF_PLUGIN_DIR} ${plugin_name}.zip 
done

#Restart grafana
systemctl restart grafana-server.service || :
