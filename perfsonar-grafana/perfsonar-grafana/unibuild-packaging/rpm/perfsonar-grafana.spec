%define install_base        /usr/lib/perfsonar
%define pkg_install_base    %{install_base}/grafana
%define httpd_config_base   /etc/httpd/conf.d

#Version variables set by automated scripts
%define perfsonar_auto_version 5.1.0
%define perfsonar_auto_relnum 0.a1.0

# defining macros needed by SELinux
# SELinux policy type - Targeted policy is the default SELinux policy used in Red Hat Enterprise Linux.
%global selinuxtype targeted
# default boolean value needs to be changed to enable http proxy
%global selinuxbooleans httpd_can_network_connect=1

Name:			perfsonar-grafana
Version:		%{perfsonar_auto_version}
Release:		%{perfsonar_auto_relnum}%{?dist}
Summary:		perfSONAR Grafana
License:		ASL 2.0
Group:			Development/Libraries
URL:			http://www.perfsonar.net
Source0:		perfsonar-grafana-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch
Requires:       perfsonar-common
Requires:       openssl
Requires:       grafana
Requires:       httpd
Requires:       mod_ssl
Requires:       curl
Requires(post): unzip
Requires(post): python3
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description
A package that installs and configures Grafana for perfSONAR

%package toolkit
Summary:		perfSONAR Grafana Toolkit Dashboards
Group:			Applications/Communications
Requires:       perfsonar-grafana

%description toolkit
A package that installs and configures perfSONAR Toolkit dashboards in Grafana

%prep
%setup -q -n perfsonar-grafana-%{version}

%build

%install
make PERFSONAR-ROOTPATH=%{buildroot}/%{pkg_install_base} HTTPD-CONFIGPATH=%{buildroot}/%{httpd_config_base} install

%clean
rm -rf %{buildroot}

%post
#Restart/enable grafana
%systemd_post grafana-server.service
if [ "$1" = "1" ]; then
    #set SELinux booleans to allow httpd proxy to work
    %selinux_set_booleans -s %{selinuxtype} %{selinuxbooleans}
    
    ######
    #if new install, then enable
    systemctl daemon-reload
    systemctl enable grafana-server.service

    #Enable and restart apache for reverse proxy
    systemctl enable httpd
    systemctl restart httpd
fi

#update grafana config - this also starts grafana
%{pkg_install_base}/grafana_config.sh

%preun
%systemd_preun grafana-server.service

%postun
%systemd_postun_with_restart grafana-server.service
if [ $1 -eq 0 ]; then
    %selinux_unset_booleans -s %{selinuxtype} %{selinuxbooleans}
fi

%files
%defattr(0644,perfsonar,perfsonar,0755)
%license LICENSE
%attr(0755, perfsonar, perfsonar) %{pkg_install_base}/grafana_config.py
%attr(0755, perfsonar, perfsonar) %{pkg_install_base}/grafana_common.sh
%attr(0755, perfsonar, perfsonar) %{pkg_install_base}/grafana_config.sh
%attr(0755, perfsonar, perfsonar) %{pkg_install_base}/grafana_plugin_download.sh
%attr(0644, perfsonar, perfsonar) %{pkg_install_base}/images/*
%attr(0644, perfsonar, perfsonar) %{pkg_install_base}/plugins/*
%attr(0644, perfsonar, perfsonar) %{httpd_config_base}/apache-grafana.conf

%files toolkit
%defattr(0644,perfsonar,perfsonar,0755)
%attr(0644, perfsonar, perfsonar) %{pkg_install_base}/dashboards/toolkit/*
%attr(0644, perfsonar, perfsonar) %{pkg_install_base}/provisioning/dashboards/toolkit.yaml
%attr(0644, perfsonar, perfsonar) %{pkg_install_base}/provisioning/datasources/exporter-metrics-local.yaml
%attr(0644, perfsonar, perfsonar) %{pkg_install_base}/provisioning/datasources/perfsonar-local.yaml

%changelog
* Tue Oct 24 2023 andy@es.net 5.0.5-0.0.a1
- Initial package