%define abiquo_basedir /opt/abiquo

Name:           abiquo-core
Version: 2.0
Release: 1%{?dist}
Url:            http://www.abiquo.com/
License:        Multiple
Group:          Development/Tools
Summary:        Abiquo Server core package 
Source0:        https://github.com/downloads/abiquo-rpms/abiquo-core/%{name}-%{version}.tar.gz
Source1:        server.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
Abiquo is the Next Generation Cloud Management Solution

This package includes core platform functionality.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%clean
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/examples/tomcat/
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/opt/vm_repository
cp -r tomcat $RPM_BUILD_ROOT/%{abiquo_basedir}
install -m 755 scripts/abiquo-tomcat.init $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/abiquo-tomcat
cp %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}/examples/tomcat/

%post
/sbin/chkconfig --add abiquo-tomcat

%preun
%{abiquo_basedir}/tomcat/bin/catalina.sh stop -force > /dev/null 2>&1
if [ $1 -eq 0 ] ; then
/sbin/chkconfig --del abiquo-tomcat
fi

%files
%{abiquo_basedir}/tomcat/bin
%{abiquo_basedir}/tomcat/lib
%{abiquo_basedir}/tomcat/logs
%{abiquo_basedir}/tomcat/temp
%{abiquo_basedir}/tomcat/LICENSE
%{abiquo_basedir}/tomcat/RUNNING.txt
%{abiquo_basedir}/tomcat/NOTICE
%{abiquo_basedir}/tomcat/RELEASE-NOTES
%{abiquo_basedir}/tomcat/webapps
%{abiquo_basedir}/tomcat/work
%{_docdir}/%{name}
/opt/vm_repository
%config(noreplace) %{abiquo_basedir}/tomcat/conf/*
%config %{_sysconfdir}/rc.d/init.d/abiquo-tomcat

%changelog
* Fri Oct 21 2011 Sergio Rubio <rubiojr@frameos.org> - 2.0-1
- Added new property managedrack
- Do not try to add limits to /etc/security/limits.conf
- Updated default remote repository location in abiquo.properties
- Apache Tomcat updated to the last 6.0.35 version

* Tue Jun 14 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8-5
- remove server/api context configs

* Tue Jun 14 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8-4
- updated default system properties

* Tue Jun 14 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8-3
- updated default system properties

* Tue May 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-2
- setup default database credentials for API/Server

* Mon May 23 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Mon Apr 18 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.6-1
- bumped version

* Mon Mar 21 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-3
- bumped release
- FIX: updated abiquo-tomcat.jar lib

* Fri Mar 04 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-2
- remove abiquo-release file 

* Fri Mar 04 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- added new properties to abiquo-tomcat.jar
- bumped version 

* Wed Mar 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-14
- remove buildstamp from release

* Tue Feb 22 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-13
- reverted port change

* Tue Feb 22 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-12
- set default port to 8080 again.
- added sample server.xml to docs dir

* Mon Feb 21 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7-11
- remove abiquo-initenv  script from abiquo-tomcat init script

* Mon Feb 07 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-10
- set buildarch to noarch

* Mon Feb 07 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-9
- fix tomcat init script JAVA_HOME path

* Mon Feb 06 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-8
- updated tomcat init script to use OpenJDK if Oracle JDK not available

* Thu Feb 03 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-7.GA
- fixed abiquo-tomcat.jar lib

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6.GA
- GA build

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5
- init script now delegates more control to abiquo-initenv

* Fri Jan 21 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- updated init script to include jpda option

* Mon Dec 20 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- revert last requires

* Fri Dec 17 2010 Sergio Rubio <srubio@abiquo.com - 1.7-2
- requires abiquo-tomcat-libs

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Thu Oct 28 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-5
- updated init script

* Thu Oct 28 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-4
- Fixed post section

* Thu Oct 28 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-3
- Increase the nofile limits

* Thu Oct 28 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-2
- Changed default tomcat port to 80

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Wed Sep 22 2010 Sergio Rubio srubio@abiquo.com 1.6.5-9
- Do not run aetk config tools if they do not exist

* Wed Sep 22 2010 Sergio Rubio srubio@abiquo.com 1.6.5-8
- Replace init script when upgrading

* Wed Sep 22 2010 Sergio Rubio srubio@abiquo.com 1.6.5-7
- Add -Dam.conversions.skip=true to abiquo-tomcat service script

* Wed Sep 22 2010 Sergio Rubio srubio@abiquo.com 1.6.5-6
- create /etc/abiquo-relase

* Mon Sep 20 2010 Sergio Rubio srubio@abiquo.com 1.6.5-5
- changes in the abiquo-tomcat service script

* Tue Sep 07 2010 Sergio Rubio srubio@abiquo.com 1.6.5-4
- changes in the abiquo-tomcat service script

* Tue Sep 07 2010 Sergio Rubio srubio@abiquo.com 1.6.5-3
- changes in the abiquo-tomcat service script

* Mon Sep 06 2010 Sergio Rubio srubio@abiquo.com 1.6.5-2
- changes in the abiquo-tomcat service script

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Tue Jul 20 2010 Sergio Rubio srubio@abiquo.com 1.6-3
- Added abiquo-tomcat init script

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Tue May 18 2010 Sergio Rubio srubio@abiquo.com 1.5.1-1
- Initial release
