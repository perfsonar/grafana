#!/bin/bash
set -e

DATASOURCE_YAML_FILES=(
    "/usr/lib/perfsonar/grafana/provisioning/datasources/perfsonar-local.yaml"
    "/usr/lib/perfsonar/grafana/provisioning/datasources/exporter-metrics-local.yaml"
)

# Check if the PERFSONAR_OPENSEARCH_URL environment variable is set.
if [ -n "${PERFSONAR_OPENSEARCH_URL}" ]; then
    for DATASOURCE_FILE in "${DATASOURCE_YAML_FILES[@]}"; do
        echo "Setting OpenSearch URL to: ${PERFSONAR_OPENSEARCH_URL} in ${DATASOURCE_FILE}"
        # Use '|' as a delimiter for sed to avoid issues with '/' in URLs.
        sed -i "s|https://localhost/opensearch|${PERFSONAR_OPENSEARCH_URL}|g" "${DATASOURCE_FILE}"
    done
fi

# Execute the original Grafana entrypoint script (/run.sh) with all passed arguments.
# This ensures that Grafana's own startup logic, as defined by its base image, is followed.
exec /run.sh "$@"