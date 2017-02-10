%define name green-recorder
%define version 1.1
%define unmangled_version 1.1
%define release 1

Summary: Record your desktop easily using a simple GUI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: M.Hanny Sabbagh <mhsabbagh@outlook.com>
Url: https://green-project.github.io/green-recorder/

%description
Record your desktop easily using a simple GUI. Built using Python, GTK+ 3 and ffmpeg. Very easy to use.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
