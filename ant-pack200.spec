%define jarname	Pack200Task

Name:		ant-pack200
Summary:	Java Pack200 External Task for Ant
Version:	0.0
Release:	%mkrel 1
Source0:	https://java-pack200-ant-task.dev.java.net/files/documents/1526/6272/ant-task.zip
Patch0:		ant-pack200-fix_build.patch
URL:		https://java-pack200-ant-task.dev.java.net/

Group:		Development/Java
License:	Sun Public License

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	java-rpmbuild
Requires:	java >= 1.5

BuildArch:	noarch

%description
JSR-200 Network Transfer Protocol reduces the download size of Java Class Files 
in a JAR. http://www.jcp.org/en/jsr/detail?id=200 This JSR has been implemented 
in Java 1.5 as set of Java APIs and Command Line Interfaces.

This project provides Ant http://ant.apache.org/ external task in order for ANT 
users to efficiently use this new feature. Ant users required easy to use Ant 
tasks for performance reasons, this project provides the external ant tasks to 
use Pack200 API effectively.

%prep
# unzip return 2 (Jonathan Bayle <mrhide@mandriva.org>, 2010-04-29)
%setup -cqT
%__cp %{SOURCE0} .
unzip ant-task.zip || true

%__rm %{jarname}.jar
%patch0 -p0

%build
export CLASSPATH="."
pushd make
%ant
popd

%install
rm -rf $RPM_BUILD_ROOT

%__install -dm 755 $RPM_BUILD_ROOT%_javadir/ant
%__install -m 644 dist/%{jarname}.jar $RPM_BUILD_ROOT%_javadir/ant/%{jarname}-%{version}.jar
ln -s %{jarname}-%{version}.jar $RPM_BUILD_ROOT%_javadir/ant/%{jarname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/*
%{_javadir}/ant/*.jar


%changelog
* Sat Oct 02 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.0-1mdv2011.0
+ Revision: 582603
- cosmetics

  + Jonathan Bayle <mrhide@mandriva.org>
    - import ant-pack200


