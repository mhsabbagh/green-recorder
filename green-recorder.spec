%global owner green-project

Name: green-recorder
Summary: A simple yet functional desktop recorder for Linux systems. Supports both Xorg server and Wayland (GNOME).
URL: https://green-project.github.io
Version: 2.5
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
تسجيل سطح المكتب بسهولة

%description
A simple yet functional desktop recorder for Linux systems. Supports both Xorg server and Wayland (GNOME).

%prep
%autosetup -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Mar 25 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.5-1
- Fix issue #22 for non-English folder names. 

* Thu Mar 09 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.4-1
- Fix glade file path (mhsabbagh@outlook.com)

* Thu Mar 09 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.3-1
- Fix #17, #18 (mhsabbagh@outlook.com)
* Thu Mar 09 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com>
- Fix #17, #18 (mhsabbagh@outlook.com)
* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.2-1
- Fix a bug making the recorder not working on non-GNOME interfaces
  (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1-1
- Fix Spec file (mhsabbagh@outlook.com)
- Version 2.0 (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com>
- Fix Spec file (mhsabbagh@outlook.com)
- Version 2.0 (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.0-1
- Added Wayland Support (GNOME Session).
- Added ability to select a specific window.
- Added ability to select a specific area.
- Added ability to show/hide mouse cursor.
- Added ability to follow mouse cursor.
- Added ability run a command after finishing recording.
- Indicator now checking for ffmpeg before running.
- Fixed some issues about multi-recordings.
- Update green-recorder (gort818@gmail.com)
- Update finding the video folder (gort818@gmail.com)
- Update green-recorder (gort818@gmail.com)
- Fix hidden icon from status bar in Wayland session (moceap@hotmail.com)
* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2-1
- new package built with tito

* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2
- Version 1.1.2. 

