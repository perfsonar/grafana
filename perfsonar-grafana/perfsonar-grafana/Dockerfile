FROM grafana/grafana:11.6.3-ubuntu

ARG PERFSONAR_ROOTPATH_ARG=/usr/lib/perfsonar/grafana
ENV PERFSONAR_ROOTPATH=${PERFSONAR_ROOTPATH_ARG}

USER root

#Create nessessary directories for Grafana provisioning
RUN mkdir -p ${PERFSONAR_ROOTPATH}
RUN mkdir -p ${PERFSONAR_ROOTPATH}/provisioning/access-control
RUN mkdir -p ${PERFSONAR_ROOTPATH}/provisioning/alerting
RUN mkdir -p ${PERFSONAR_ROOTPATH}/provisioning/notifiers
RUN mkdir -p ${PERFSONAR_ROOTPATH}/provisioning/plugins
RUN mkdir -p ${PERFSONAR_ROOTPATH}/dashboards/empty

#Copy perfSONAR Grafana files
COPY images/ /usr/share/grafana/public/img/
COPY provisioning/dashboards/ ${PERFSONAR_ROOTPATH}/provisioning/dashboards/
COPY provisioning/datasources/ ${PERFSONAR_ROOTPATH}/provisioning/datasources/
COPY dashboards/ ${PERFSONAR_ROOTPATH}/dashboards/

RUN chown -R grafana:root ${PERFSONAR_ROOTPATH}

#Make the provisioned dashboards and datasources editable through the user interface
RUN sed -i ${PERFSONAR_ROOTPATH}/provisioning/dashboards/*.yaml -e 's/allowUiUpdates: false/allowUiUpdates: true/g'
RUN sed -i ${PERFSONAR_ROOTPATH}/provisioning/datasources/*.yaml -e 's/editable: false/editable: true/g'

# This script will run before Grafana starts to modify the datasource URLs.
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# The original Grafana CMD (which starts Grafana) will now be passed as arguments to our entrypoint script.
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

USER grafana
EXPOSE 3000

