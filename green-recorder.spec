%global owner green-project

Name: green-recorder
Summary: Simply Desktop Recording
Summary(ar): تسجيل سطح المكتب بيسر
URL: https://green-project.github.io
Version: 1.2
Release: 1%{?dist}
Source: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildArch: noarch

BuildRequires: python2-devel
Requires: python2
Requires: python2-pydbus
Requires: ffmpeg
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




# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2017 Mosaab Alzoubi <moceap@hotmail.com> -->
<!--
EmailAddress: moceap@hotmail.com
SentUpstream: 2017-2-14
-->
<application>
  <id type="desktop">%{name}.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Simply Desktop Recording</summary>
  <summary xml:lang="ar">تسجيل سطح المكتب بيسر</summary>
  <description>
    <p>
	Simply Desktop Recording.
    </p>
  </description>
  <description xml:lang="ar">
    <p>
	تسجيل سطح المكتب بيسر.
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
* Tue Feb 14 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-1
- Version 1.2
