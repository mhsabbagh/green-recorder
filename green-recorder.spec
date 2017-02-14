%global owner green-project

Name: green-recorder
Summary: A simple yet functional desktop recorder for Linux systems. 
URL: https://green-project.github.io
Version: 1.1.1
Release: 1%{?dist}
Source: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildArch: noarch

BuildRequires: python2-devel
Requires: python2
Requires: python2-pydbus
Requires: ffmpeg
Requires: gawk
Requires: libappindicator-gtk3
Requires: rpmfusion-free-release 

%description -l ar
تسجيل سطح المكتب بيسر

%description
Simply Desktop Recording

%prep
%autosetup -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<application>
  <id type="desktop">%{name}.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A simple desktop recorder. Built using ffmpeg, Python and GTK+ 3.</summary>
  <description>
    <p>
	Simply Desktop Recording.
    </p>
  </description>
  <url type="homepage">https://green-project.github.io</url>
  <screenshots>
    <screenshot type="default">https://camo.githubusercontent.com/1b2a0354688469a5b88f7c300b830cc6395cc6f3/687474703a2f2f692e696d6775722e636f6d2f76684a7078496c2e706e67</screenshot>
  </screenshots>
  <updatecontact>mhsabbagh@outlook.com</updatecontact>
</application>
EOF

%files
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
- Version 1.1.1
