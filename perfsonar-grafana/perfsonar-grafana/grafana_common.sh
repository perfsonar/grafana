#!/bin/bash

#System arch which is useful in some of the URLs
ARCH=$(uname -m | sed -e 's/x86_64/amd64/')

#
# PLUGINS_TO_INSTALL: Associative array that maps local name to download URL
declare -A PLUGINS_TO_INSTALL
PLUGINS_TO_INSTALL[grafana-opensearch-datasource]="https://grafana.com/api/plugins/grafana-opensearch-datasource/versions/2.13.1/download?os=linux&arch=${ARCH}"
PLUGINS_TO_INSTALL[grafana-esnet-matrix-panel-viz]="https://grafana.com/api/plugins/esnet-matrix-panel/versions/1.0.9/download"

##
# PLUGINS_TO_REMOVE: Array with the names of the unzipped directories to be removed on install. 
# In general all plugins should be in this list so every update adds a fresh copy. Keeping separate allows us to remove plugins we no longer want installed as well.
PLUGINS_TO_REMOVE=( esnet-matrix-panel grafana-opensearch-datasource )
