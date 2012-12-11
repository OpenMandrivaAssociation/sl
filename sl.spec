%define name    sl
%define version 5.1
%define release %mkrel 8

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Mistyping correcter
License:        Public Domain
Group:          Toys
URL:            http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/
Source0:        http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/sl/%{name}.tar.bz2
Source1:        %{name}.en.1.bz2
Patch0:		http://www.linet.gr.jp/~izumi/sl/%{name}5-1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildRequires:  ncurses-devel
BuildRequires:  termcap-devel

%description
sl is a sophisticated graphical program which corrects your mistyping.

%prep
%setup -q -n %{name}
bzcat %{SOURCE1} > %{name}.en.1
%patch0 -p 1

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 sl %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 sl.en.1 %{buildroot}%{_mandir}/man1/sl.1

install -d -m 755 %{buildroot}%{_mandir}/ja/man1
install -m 644 sl.1 %{buildroot}%{_mandir}/ja/man1/sl.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.patch5
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/ja/man1/*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 5.1-8mdv2010.0
+ Revision: 433920
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 5.1-7mdv2009.0
+ Revision: 260782
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 5.1-6mdv2009.0
+ Revision: 252563
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 5.1-4mdv2008.1
+ Revision: 127356
- kill re-definition of %%buildroot on Pixel's request


* Thu Oct 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 5.1-4mdk
- Fix BuildRequires

* Wed Oct 19 2005 Nicolas Lécureuil <neoclust@mandriva.org> 5.1-3mdk
- Fix BuildRequires
- %%mkrel

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.1-2mdk 
- fix man page
- fix description and summary (Adam Williamson <awilliamson@mandriva.com>)

* Fri Jun 10 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.1-1mdk 
- first release, inspirated from gentoo

