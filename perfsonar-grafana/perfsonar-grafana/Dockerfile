FROM grafana/grafana:12.4-ubuntu

COPY . /usr/lib/perfsonar/grafana

USER root

#Setup provisioning
RUN mkdir -p /usr/lib/perfsonar/grafana/dashboards/empty
RUN cp -r /usr/lib/perfsonar/grafana/images/* /usr/share/grafana/public/img/
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/dashboards/*.yaml -e 's/allowUiUpdates: false/allowUiUpdates: true/g'

# Setup datasource to use environment variable for URL, defaulting to localhost if not set
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/datasources/*.yaml -e 's|\( *\)url:.*|\1url: ${OPENSEARCH_URL}|'
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/datasources/*.yaml -e 's|\( *\)version: "2.6.0"|\1version: "${OPENSEARCH_VERSION}"|' 

USER grafana
EXPOSE 3000

