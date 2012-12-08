Summary:	The Manbo rpm configuration and scripts
Name:		rpm-manbo-setup
Version:	2
Release:	27
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


%changelog
* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 2-26
+ Revision: 651378
+ rebuild (emptylog)

* Wed Apr 06 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2-25
+ Revision: 650979
- cleanups

* Wed Mar 30 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2-24
+ Revision: 649320
- add -Wstrict-aliasing=2 to %%debugcflags (#42900)
- drop rpmrc, rpmpopt & rpmb_deprecated
- add -frecord-gcc-switches to debugcflags
- drop macros that are either deprecated or duplicates of upstream definitions

* Sun Dec 05 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2-23mnb2
+ Revision: 609608
- pass '--enable-new-dtags' to %%{ldflags}

* Sat Oct 16 2010 Matthew Dawkins <mattydaw@mandriva.org> 2-22mnb2
+ Revision: 585917
- change compression extension from lzma to xz
- changed compression extension from lzma to xz

* Tue Apr 27 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2-21mnb2
+ Revision: 539421
- add --build-id to default linker flags (closes #58487)
- add a %%EVRD macro for use with versioned provides/requires to automatically add all the tags used for version comparison.

* Fri Nov 27 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 2-19mnb2
+ Revision: 470600
- add '-Wl,-O1' to linker flags

  + Christophe Fergeau <cfergeau@mandriva.com>
    - remove -fexceptions from default cflags

* Mon Sep 28 2009 Anssi Hannula <anssi@mandriva.org> 2-18mnb2
+ Revision: 450575
- Fix %%__libtool_configure macro relying on apparently wrong behaviour
  of old bash versions. This caused %%configure macro to fail with configure
  scripts not generated with autotools when using a new enough bash. (see
  http://lists.mandriva.com/cooker/2009-09/msg00727.php,
  http://www.opengroup.org/austin/mailarchives/ag/msg18258.html)

* Thu Sep 24 2009 Olivier Blin <oblin@mandriva.com> 2-17mnb2
+ Revision: 448369
- fix mips* compile flags (from Arnaud Patard)
- add arm* compile flags (from Arnaud Patard)
- use armv5tl by default, don't use armv5tel as some SoC have broken
  instructions in the "e" extension (from Arnaud Patard)
- improve release computed in bootstrap (from Arnaud Patard)

* Wed Jan 28 2009 Pixel <pixel@mandriva.com> 2-16mnb2
+ Revision: 334795
- add fix-libtool-from-moving-options-after-libs and run it before configure; it
  will modify libtool in configure to correctly pass -Wl,xxx options before
  libraries

* Tue Jan 27 2009 Pixel <pixel@mandriva.com> 2-15mnb2
+ Revision: 334082
- do not call cputoolize anymore in %%configure
  (since it is unneeded since September 2003, cf libtool.spec)

* Mon Dec 15 2008 Pixel <pixel@mandriva.com> 2-14mnb2
+ Revision: 314545
- link with "-z relro" by default (cf "Gentoo Hardened Toolchain" for info)
- have -Werror=format-security by default in %%optflags

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2-13mnb2
+ Revision: 265652
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Pixel <pixel@mandriva.com> 2-12mnb2
+ Revision: 217356
- when modifying libtool, use plain echo instead of $echo since some old libtool use $ECHO instead

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 2-11mnb2
+ Revision: 217017
- create %%ldflags out of %%setup_compile_flags (as suggested by Anssi on cooker ml)

* Fri Jun 06 2008 Pixel <pixel@mandriva.com> 2-10mnb2
+ Revision: 216518
- create %%setup_compile_flags to be used in %%cmake

* Wed Jun 04 2008 Anssi Hannula <anssi@mandriva.org> 2-9mnb2
+ Revision: 214913
- add fix-dlsearch-path-in-libtool-for-multilib and run it before
  configure; it will modify libtool run-time library search path
  definition in configure script for lib64 compliance if configure was
  generated with a libtool version that had "/usr/lib /lib" hardcoded;
  this will prevent libtool from adding invalid rpath when linking
  against libraries in standard lib64 library directories

* Mon Jun 02 2008 Pixel <pixel@mandriva.com> 2-8mnb2
+ Revision: 214232
- revert to upstream default %%_localstatedir (/var instead of /var/lib) (#22312)

* Mon May 26 2008 Pixel <pixel@mandriva.com> 2-7mnb2
+ Revision: 211347
- create %%before_configure when %%configure nor %%configure2_5x can be used
  (it also factorizes duplication between %%configure and %%configure2_5x)

* Fri May 23 2008 Pixel <pixel@mandriva.com> 2-6mnb2
+ Revision: 210340
- when forcing ld option "--no-undefined", modify ltmain.sh to discard
  --no-undefined when building share library modules (ie plugins)

* Wed May 21 2008 Pixel <pixel@mandriva.com> 2-5mnb2
+ Revision: 209770
- have ld option "--as-needed" and --no-undefined" by default
  (to workaround, define %%_disable_ld_as_needed or %%_disable_ld_no_undefined)

* Wed May 21 2008 Pixel <pixel@mandriva.com> 2-4mnb2
+ Revision: 209757
- when using as-needed, add to existing LDFLAGS

* Tue May 20 2008 Pixel <pixel@mandriva.com> 2-3mnb2
+ Revision: 209464
- setting %%_enable_as_needed adds --as-needed and --no-undefined to ld calls
  (added through LDFLAGS with -Wl when calling %%configure)
- it also forces --as-needed in libtool for shared libraries
  (to workaround a libtool bug, cf http://lists.gnu.org/archive/html/libtool-patches/2004-06/msg00002.html)

* Wed May 07 2008 Pixel <pixel@mandriva.com> 2-2mnb2
+ Revision: 202856
- call fix-libtool-ltmain-from-overlinking in %%configure and %%configure2_5x to
  prevent libtool overlinking (cf http://wiki.mandriva.com/en/Overlinking)
- manbo_release is now 2

* Fri Mar 28 2008 Pixel <pixel@mandriva.com> 0.6-1mnb1
+ Revision: 190833
- remove duplicated space in %%optflags (otherwise gdb build breaks)

* Fri Feb 22 2008 Pixel <pixel@mandriva.com> 0.5-1mnb1
+ Revision: 173824
- replace %%mkrel with %%manbo_mkrel for Manbo Core 1

* Fri Feb 15 2008 Pixel <pixel@mandriva.com> 0.5-1mdv2008.1
+ Revision: 169009
- 0.5: move enough macros here from rpm-mandriva-setup to correctly define
  macros %%configure, %%optflags and %%_install_info

* Fri Feb 15 2008 Pixel <pixel@mandriva.com> 0.4-1mdv2008.1
+ Revision: 168823
- move macros needed for Manbo packages here out of rpm-mandriva-setup

* Fri Feb 15 2008 Pixel <pixel@mandriva.com> 0.3-1mdv2008.1
+ Revision: 168743
- rpmb_deprecated must be executable

* Thu Feb 14 2008 Pixel <pixel@mandriva.com> 0.2-1mdv2008.1
+ Revision: 167745
- rpmb_deprecated must be in /usr/lib/rpm

* Thu Feb 14 2008 Pixel <pixel@mandriva.com> 0.1-1mdv2008.1
+ Revision: 167720
- initial package (with files moved from rpm-mandriva-setup)
- Created package structure for rpm-manbo-setup.

