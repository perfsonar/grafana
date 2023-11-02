# perfSONAR Grafana Configuration

This is a set of packages to configure [Grafana](https://grafana.com/) and install dashboards, data sources and other resources used by perfSONAR. 

# Editing Dashboards
This repository provides a Docker setup that runs Grafana and installs the dashboards in an editable mode. The datasources are updated to point at a development archive so you also have data with which to work. To use the development environment perform the following steps:

1. Run the following to start the container:
```
cd perfsonar-grafana/perfsonar-grafana
docker compose up --build -d
```
2. Open your web browser to http://localhost:3000
3. Login with user/pass *admin/admin* (in case its not obvious, use this for a local dev environment, not production).
4. Change the password on the next screen if you so desire.
5. Navigate to the dashboard you want to edit
6. Make your changes and save.
7. To export to git, in the UI on the dashboard to export click the Share icon, click the Export tab then click "View JSON" to see the JSON.
8. Copy and paste the JSON to the appropriate file in the `dashboards` subdirectory.

# Updating Grafana Version
The `grafana` subdirectory grabs the Grafana RPM and Debian packages of the version that is ships with perfSONAR. In `grafana/packages.yaml` update the URLs and file names with the new version of Grafana to grab a new version.

# Adding/Updating Grafana Plugins
The build process of the perfsonar-grafana package downloads certain plugins since many users install perfSONAR on hosts without general internet the variable in `perfsonar-grafana/perfsonar-grafana/grafana_common.sh` with the new plugin information. See the comments in that file for more details.