%define name    sl
%define version 5.1
%define release %mkrel 4

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

