%define name rpm-manbo-setup
%define version 2
%define release %manbo_mkrel 24

# for bootstrapping purpose:
%if "%{?manbo_mkrel:has_manbo}" == ""
%define manbo_mkrel(c:) %{-c: 0.%{-c*}.}%{1}%{?subrel:.%subrel}mnb1
%endif

Summary: The Manbo rpm configuration and scripts
Name: %{name}
Version: %{version}
Release: %{release}
Source3: manbo.macros
Source4: manbo-build.macros
Source5: fix-libtool-ltmain-from-overlinking
Source6: force-as-needed-for-shared-lib-in-libtool
Source7: drop-ld-no-undefined-for-shared-lib-modules-in-libtool
Source8: fix-dlsearch-path-in-libtool-for-multilib
Source9: fix-libtool-from-moving-options-after-libs
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
install %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 %buildroot/usr/lib/rpm/manbo

install -D -m 644 %SOURCE3 %buildroot/etc/rpm/macros.d/10manbo.macros
install -D -m 644 %SOURCE4 %buildroot/etc/rpm/macros.d/10manbo-build.macros

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/rpm/macros.d
%{_sysconfdir}/rpm/macros.d/10manbo.macros
%dir %_prefix/lib/rpm/manbo

%files build
%{_sysconfdir}/rpm/macros.d/10manbo-build.macros
%_prefix/lib/rpm/manbo/fix-libtool-ltmain-from-overlinking
%_prefix/lib/rpm/manbo/force-as-needed-for-shared-lib-in-libtool
%_prefix/lib/rpm/manbo/drop-ld-no-undefined-for-shared-lib-modules-in-libtool
%_prefix/lib/rpm/manbo/fix-dlsearch-path-in-libtool-for-multilib
%_prefix/lib/rpm/manbo/fix-libtool-from-moving-options-after-libs
