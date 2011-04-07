Summary:	The Manbo rpm configuration and scripts
Name:		rpm-manbo-setup
Version:	2
Release:	26
Source3:	manbo.macros
Source4:	manbo-build.macros
Source5:	fix-libtool-ltmain-from-overlinking
Source6:	force-as-needed-for-shared-lib-in-libtool
Source7:	drop-ld-no-undefined-for-shared-lib-modules-in-libtool
Source8:	fix-dlsearch-path-in-libtool-for-multilib
Source9:	fix-libtool-from-moving-options-after-libs
License:	GPL
Group:		System/Configuration/Packaging
BuildArch:	noarch

%description
The Manbo rpm configuration and scripts.

%package	build
Group:		System/Configuration/Packaging
Summary:	The Manbo rpm configuration and scripts to build rpms
Requires:	%name = %version-%release

%description	build
The Manbo rpm configuration and scripts dedicated to build rpms.

%install
install -d %buildroot/usr/lib/rpm/manbo
install %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 %buildroot/usr/lib/rpm/manbo

install -D -m 644 %SOURCE3 %buildroot/etc/rpm/macros.d/10manbo.macros
install -D -m 644 %SOURCE4 %buildroot/etc/rpm/macros.d/10manbo-build.macros

%files
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
