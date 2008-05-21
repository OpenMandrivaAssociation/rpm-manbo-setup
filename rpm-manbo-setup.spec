%define name rpm-manbo-setup
%define version 2
%define release %manbo_mkrel 5

# for bootstrapping purpose:
%if "%{?manbo_mkrel:has_manbo}" == ""
%define manbo_mkrel(c:) %{1}
%endif

Summary: The Manbo rpm configuration and scripts
Name: %{name}
Version: %{version}
Release: %{release}
Source0: rpmrc
Source1: rpmpopt
Source2: rpmb_deprecated
Source3: manbo.macros
Source4: manbo-build.macros
Source5: fix-libtool-ltmain-from-overlinking
Source6: force-as-needed-for-shared-lib-in-libtool
License: GPL
Group: System/Configuration/Packaging
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
The Manbo rpm configuration and scripts.

%package build
Group: System/Configuration/Packaging
Summary: The Manbo rpm configuration and scripts to build rpms
Requires: %name = %version-%release

%description build
The Manbo rpm configuration and scripts dedicated to build rpms.

%install
rm -rf %buildroot
install -d %buildroot/usr/lib/rpm/manbo
install -m 644 %SOURCE0 %SOURCE1 %buildroot/usr/lib/rpm/manbo
install %SOURCE5 %SOURCE6 %buildroot/usr/lib/rpm/manbo
install %SOURCE2 %buildroot/usr/lib/rpm

install -D -m 644 %SOURCE3 %buildroot/etc/rpm/macros.d/10manbo.macros
install -D -m 644 %SOURCE4 %buildroot/etc/rpm/macros.d/10manbo-build.macros

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/rpm/macros.d
%{_sysconfdir}/rpm/macros.d/10manbo.macros
%dir %_prefix/lib/rpm/manbo
%_prefix/lib/rpm/manbo/rpmpopt
%_prefix/lib/rpm/manbo/rpmrc
%_prefix/lib/rpm/rpmb_deprecated

%files build
%{_sysconfdir}/rpm/macros.d/10manbo-build.macros
%_prefix/lib/rpm/manbo/fix-libtool-ltmain-from-overlinking
%_prefix/lib/rpm/manbo/force-as-needed-for-shared-lib-in-libtool
