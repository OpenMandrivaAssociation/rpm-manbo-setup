%define name rpm-manbo-setup
%define version 0.2
%define release %mkrel 1

Summary: The Manbo rpm configuration and scripts
Name: %{name}
Version: %{version}
Release: %{release}
Source0: rpmrc
Source1: rpmpopt
Source2: rpmb_deprecated
License: GPL
Group: System/Configuration/Packaging
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
The Manbo rpm configuration and scripts.

%install
rm -rf %buildroot
install -d %buildroot/usr/lib/rpm/manbo
install -m 644 %SOURCE0 %SOURCE1 %buildroot/usr/lib/rpm/manbo
install -m 644 %SOURCE2 %buildroot/usr/lib/rpm

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%_prefix/lib/rpm/manbo
%_prefix/lib/rpm/rpmb_deprecated
