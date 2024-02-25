FROM grafana/grafana:10.3.1-ubuntu

COPY . /usr/lib/perfsonar/grafana

USER root
#Setup provisioning
RUN mkdir -p /usr/lib/perfsonar/grafana/dashboards/empty
RUN  cp -r /usr/lib/perfsonar/grafana/images/* /usr/share/grafana/public/img/
RUN sed -i /usr/lib/perfsonar/grafana/provisioning/dashboards/*.yaml -e 's/allowUiUpdates: false/allowUiUpdates: true/g'
#Uncomment below to point datasource at different MA by default
#RUN sed -i /usr/lib/perfsonar/grafana/provisioning/datasources/*.yaml -e 's/localhost/34.171.24.112/g'

USER grafana
EXPOSE 3000

