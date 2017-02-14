%global owner green-project

Name: green-recorder
Summary: A simple yet functional desktop recorder for Linux systems. 
URL: https://green-project.github.io
Version: 1.1.2
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
Requires: python2-urllib3
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
	A simple yet functional desktop recorder for Linux systems.
    </p>
  </description>
  <url type="homepage">https://green-project.github.io</url>
  <screenshots>
    <screenshot type="default">http://i.imgur.com/vhJpxIl.png</screenshot>
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
* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2-1
- new package built with tito

* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2
- Version 1.1.2. 

