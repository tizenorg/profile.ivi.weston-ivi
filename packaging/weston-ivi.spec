Name:       weston-ivi
Version:    1
Release:    0
Summary:    Tizen IVI Weston configuration and set-up
License:    MIT
Group:      Automotive/Configuration
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Source1001: weston-ivi.manifest
Provides:   weston-startup

%description
This package contains Tizen IVI-specific set-up for the Weston
compositor, including systemd unit files, etc.

%package config
Summary:    Tizen IVI Weston configuration
Group:      Automotive/Configuration
Requires:   weekeyboard
Conflicts:  ico-uxf-weston-plugin
%description config
This package contains Tizen IVI-specific configuration for the Weston
compositor.

%package config-modello
Summary:    Tizen IVI Modello Weston configuration
Group:      Automotive/Configuration
Requires:   weekeyboard
Conflicts:  ico-uxf-weston-plugin, weston-ivi-config
%description config-modello
This package contains Tizen IVI-specific Modello configuration for the Weston
compositor.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install

install -d %{buildroot}%{_unitdir_user}/weston.target.wants
install -m 644 weston.service %{buildroot}%{_unitdir_user}/weston.service
ln -sf ../weston.service %{buildroot}/%{_unitdir_user}/weston.target.wants/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -m 0644 weston.sh %{buildroot}%{_sysconfdir}/profile.d/

%define weston_config_dir %{_sysconfdir}/xdg/weston
mkdir -p %{buildroot}%{weston_config_dir}
install -m 0644 weston.ini %{buildroot}%{weston_config_dir}
install -m 0644 weston-modello.ini %{buildroot}%{weston_config_dir}/weston-modello.ini

%post config-modello
ln -s %{weston_config_dir}/weston-modello.ini %{weston_config_dir}/weston.ini


%postun config-modello
rm %{weston_config_dir}/weston.ini

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_unitdir_user}/weston.service
%{_unitdir_user}/weston.target.wants/weston.service
%config %{_sysconfdir}/profile.d/*

%files config
%manifest %{name}.manifest
%config %{weston_config_dir}/weston.ini

%files config-modello
%manifest %{name}.manifest
%config %{weston_config_dir}/weston-modello.ini
