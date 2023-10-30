#!/bin/bash

#include shared vars
. $(dirname $0)/grafana_common.sh 

PLUGIN_PATH=$1
for plugin_name in "${!PLUGINS_TO_INSTALL[@]}"
do
    curl -k -Ss -L -o ${PLUGIN_PATH}/${plugin_name}.zip ${PLUGINS_TO_INSTALL[${plugin_name}]}
done