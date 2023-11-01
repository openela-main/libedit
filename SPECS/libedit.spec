%global snap 20210216
%global dir_snap 20210216

Summary:	The NetBSD Editline library
Name:		libedit
Version:	3.1
Release:	37.%{snap}cvs%{?dist}
License:	BSD
URL:		https://www.thrysoee.dk/editline/
Source0:	https://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	groff-base
BuildRequires:	make
BuildRequires:	ncurses-devel

%description
Libedit is an autotool- and libtoolized port of the NetBSD Editline library.
It provides generic line editing, history, and tokenization functions, similar
to those found in GNU Readline.

%package devel
Summary:	Development files for %{name}

Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	ncurses-devel%{?_isa}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -n %{name}-%{dir_snap}-%{version}

# Fix unused direct shared library dependencies.
sed -i "s/lncurses/ltinfo/" configure

%build
%configure --disable-static --disable-silent-rules

%make_build

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
# See rhbz#1349671
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/history.3*

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog THANKS
%{_mandir}/man5/editrc.5*
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files devel
%doc examples/fileman.c examples/tc1.c examples/wtc1.c
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_includedir}/histedit.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_includedir}/editline
%{_includedir}/editline/readline.h

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.1-37.20210216cvs
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.1-36.20210216cvs
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Feb 16 2021 Jerry James <loganjerry@gmail.com> - 3.1-35.20210216cvs
- New version (20210216-3.1)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-34.20191231cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-33.20191231cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-32.20191231cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Jerry James <loganjerry@gmail.com> - 3.1-31.20191231cvs
- New version (20191231-3.1)

* Wed Dec 11 2019 Jerry James <loganjerry@gmail.com> - 3.1-30.20191211cvs
- New version (20191211-3.1)

* Sat Oct 26 2019 Jerry James <loganjerry@gmail.com> - 3.1-29.20191025cvs
- New version (20191025-3.1)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-28.20190324cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Jerry James <loganjerry@gmail.com> - 3.1-27.20190324cvs
- New version (20190324-3.1), fixes bz 1677247

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-26.20181209cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jerry James <loganjerry@gmail.com> - 3.1-25.20181209cvs
- New version (20181209-3.1)
- ChangeLog is now UTF-8, so drop conversion from ISO8859-1
- Drop man page fix, fixed upstream
- Drop pkgconfig file fix, fixed upstream
- Add groff-base BR for man page generation

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-24.20170329cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 3.1-23.20170329cvs
- Add gcc BR
- Build verbosely
- Drop obsolete --enable-widec configure option
- Fix "unused direct shared library dependency" warning from rpmlint again
- Fix man page error due to BSD nroff macro that is not available on Linux
- Drop explicit R on pkgconfig from the -devel package, autogenerated

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-22.20170329cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1-21.20170329cvs
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-20.20170329cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-19.20170329cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Boris Ranto <branto@redhat.com> - 0:3.1-18.20170329cvs
- New version (0:3.1-18.20170329cvs)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-17.20160618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Boris Ranto <branto@redhat.com> - 0:3.1-16.20160618cvs
- Fix file conflict with readline (rhbz#1349671)

* Tue Jun 21 2016 Boris Ranto <branto@redhat.com> - 0:3.1-15.20160618cvs
- New version (0:3.1-15.20160618)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14.20150325cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-13.20150325cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Boris Ranto <branto@redhat.com> - 3.1-12.20150325cvs
- Rebase to latest upstream version
- We no longer need the patch to not ignore extchars on utf8 charset -- the patch was merged upstream

* Wed Mar 25 2015 Boris Ranto <branto@redhat.com> - 3.1-11.20141030cvs
- change the format of patches
- hide protected functions from other modules

* Wed Mar 18 2015 Boris Ranto <branto@redhat.com> - 3.1-10.20141030cvs
- ignore external characters in input only if not utf8

* Mon Jan 12 2015 Boris Ranto <branto@redhat.com> - 3.1-9.20141030cvs
- Rebase to latest upstream release
- Fix rhbz#1180529

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-8.20140213cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Tom Callaway <spot@fedoraproject.org> - 3.1-7.20140213cvs
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6.20140213cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Kamil Dudka <kdudka@redhat.com> - 3.1-1.20140213cvs
- Update to 20140213-3.1

* Tue Jan 21 2014 Kamil Dudka <kdudka@redhat.com> - 3.1-4.20130712cvs
- Avoid SIGSEGV in clear_history() if called prior to using_history() (#1055409)

* Thu Jan 02 2014 Kamil Dudka <kdudka@redhat.com> - 3.1-3.20130712cvs
- Update to 20130712-3.1 (#1045675)
- Do not mark man pages as %%doc (#1045675)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2.20130601cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Kamil Dudka <kdudka@redhat.com> - 3.1-1.20130601cvs
- Update to 20121213-3.1 (#970084)

* Wed Feb 20 2013 Kamil Dudka <kdudka@redhat.com> - 3.0-10.20121213cvs
- Update to 20121213-3.0 (#912957)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9.20120601cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 28 2012 Kamil Dudka <kdudka@redhat.com> - 3.0-8.20110802cvs
- fix specfile issues reported by the fedora-review script

* Wed Jul 18 2012 Kamil Dudka <kdudka@redhat.com> 3.0-7.20120601cvs
- Update to 3.0 (20120601 snap)
- fix crash of el_insertstr() on incomplete multi-byte sequence (#840598)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6.20110802cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Kamil Dudka <kdudka@redhat.com> - 3.0-5.20110802cvs
- fix code defects found by Coverity

* Wed Nov  9 2011 Adam Williamson <awilliam@redhat.com> 3.0-4.20110802cvs
- rebuild to keep it 'newer' than the f15 and f16 builds

* Fri Aug 26 2011 Kamil Dudka <kdudka@redhat.com> 3.0-3.20110802cvs
- Update to 3.0 (20110802 snap), fixes #732989

* Thu Mar 24 2011 Jerry James <loganjerry@gmail.com> - 3.0-3.20110227cvs
- Update to 3.0 (20110227 snap)
- Drop upstreamed -sigwinch patch
- Preserve ChangeLog timestamp when converting to UTF-8
- Fix "unused direct shared library dependency" warning from rpmlint
- Don't BR gawk; it is on the exceptions list

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3.20100424cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Jerry James <loganjerry@gmail.com> - 3.0-2.20100424cvs
- Update to 3.0 (20100424 snap)
- Enable wide-character (Unicode) support

* Tue Mar 30 2010 Kamil Dudka <kdudka@redhat.com> 3.0-2.20090923cvs
- eliminated compile-time warnings
- fix to not break the read loop on SIGWINCH, patch contributed
  by Edward Sheldrake (#575383)

* Tue Nov 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0-1.20090923cvs
- Update to 3.0 (20090923 snap)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4.20080712cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3.20080712cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.11-2.20080712cvs
- Add ncurses-devel requires to -devel subpackage (BZ#481252)

* Sun Jul 27 2008 Debarshi Ray <rishi@fedoraproject.org> - 2.11-1.20080712cvs
- Version bump to 20080712-2.11.

* Sat Feb 16 2008 Debarshi Ray <rishi@fedoraproject.org> - 2.10-4.20070831cvs
- Rebuilding with gcc-4.3 in Rawhide.

* Sun Nov 04 2007 Debarshi Ray <rishi@fedoraproject.org> - 2.10-3.20070831cvs
- Removed 'Requires: ncurses-devel'.

* Sat Nov 03 2007 Debarshi Ray <rishi@fedoraproject.org> - 2.10-2.20070831cvs
- Changed character encoding of ChangeLog from ISO8859-1 to UTF-8.

* Sun Sep 02 2007 Debarshi Ray <rishi@fedoraproject.org> - 2.10-1.20070831cvs
- Initial build. Imported SPEC from Rawhide.
