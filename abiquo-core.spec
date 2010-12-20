%define abiquo_basedir /opt/abiquo

Name:           abiquo-core
Version: 1.7
Release: 3%{?dist}%{?buildstamp}
Url:            http://www.abiquo.com/
License:        Multiple
Group:          Development/Tools
Summary:        Abiquo Server core package 
Source0:        %{name}-%{version}.tar.gz
Source1:        abiquo-release
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/opt/vm_repository
cp -r tomcat $RPM_BUILD_ROOT/%{abiquo_basedir}
install -m 755 scripts/abiquo-tomcat.init $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/abiquo-tomcat
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/

%post
/sbin/chkconfig --add abiquo-tomcat
echo "root soft nofile 4096" >> /etc/security/limits.conf
echo "root hard nofile 10240" >> /etc/security/limits.conf

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
%{_sysconfdir}/abiquo-release

%changelog
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