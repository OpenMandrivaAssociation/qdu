%define name qdu
%define version 2.2
%define release %mkrel 3

Summary:	Graphical Disk Usage
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Monitoring
Source:		http://artis.imag.fr/Membres/Gilles.Debunne/Code/QDU/qdu.tar.gz
URL:		http://artis.imag.fr/Membres/Gilles.Debunne/Code/QDU/
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  libqt-devel
Provides:	Xdu
Obsoletes:	Xdu

%description
A disk usage with a graphical front-end based on Trolltech Qt.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%_prefix/lib/qt3/bin/qmake qdu.pro
%make

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_bindir}
%{__install} --mode=755 qdu $RPM_BUILD_ROOT%{_bindir}

(cd $RPM_BUILD_ROOT
mkdir -p .%{_menudir}
cat > .%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/%{name}"\
icon="monitoring_section.png"\
title="Qdu"\
longtitle="Graphical Disk Usage"\
needs="x11"\
section="System/Monitoring"
EOF
)

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG INSTALL LICENCE README
%{_bindir}/*
%{_menudir}/%name

