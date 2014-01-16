%define _unitdir_user /usr/lib/systemd/user

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
%description config
This package contains Tizen IVI-specific configuration for the Weston
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
