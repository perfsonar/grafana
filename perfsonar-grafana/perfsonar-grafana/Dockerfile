FROM grafana/grafana:10.2.0-ubuntu

COPY . /usr/lib/perfsonar/grafana

USER root
#Install base dependencies and install custom plugins
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/dashboards/*.yaml -e 's/allowUiUpdates: false/allowUiUpdates: true/g'
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/datasources/*.yaml -e 's/localhost/34.171.24.112/g'

USER grafana
EXPOSE 3000

