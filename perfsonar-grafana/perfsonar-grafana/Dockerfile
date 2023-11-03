FROM grafana/grafana:10.2.0-ubuntu

COPY . /usr/lib/perfsonar/grafana

USER root
#Setup provisioning
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/dashboards/*.yaml -e 's/allowUiUpdates: false/allowUiUpdates: true/g'
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/datasources/*.yaml -e 's/localhost/34.171.24.112/g'
RUN mkdir -p /usr/lib/perfsonar/grafana/dashboards/empty

USER grafana
EXPOSE 3000

