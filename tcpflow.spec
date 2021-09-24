#
# Conditional build:
%bcond_with	cairo		# disable Cairo even if present

Summary:	TCP Flow Recorder
Summary(pl.UTF-8):	Program zapisujący ruch TCP
Name:		tcpflow
Version:	1.5.2
Release:	2
License:	GPL v3
Group:		Applications/Networking
Source0:	http://ftp.debian.org/debian/pool/main/t/tcpflow/%{name}_%{version}+repack1.orig.tar.gz
# Source0-md5:	4348cdfa9e1d61a459d1f696204fbeff
Patch0:		0001-using-the-debian-package-of-libhttp-parser-instead-o.patch
URL:		https://github.com/simsong/tcpflow
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
%{?with_cairo:BuildRequires:	cairo-devel}
#BuildRequires:	exiv2-devel
BuildRequires:	expat-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	http-parser-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	libmd-devel
BuildRequires:	libpcap-devel
#BuildRequires:	libregex-devel
#BuildRequires:	lightgrep-devel
BuildRequires:	openssl-devel
BuildRequires:	pixman-devel
BuildRequires:	sqlite3-devel
BuildRequires:	tre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpflow is program that captures data transmitted as part of TCP
connections, and and stores the data in a way that is convenient for
protocol analysis or debugging. Tcpflow stores all captured data in
two files per connection.

%description -l pl.UTF-8
Tcpflow jest programem, który przechwytuje dane przesyłane w ramach
połączeń TCP i zapisuje je w sposób wygodny do analizy lub śledzenia
protokołu - tworząc dwa pliki z danymi na każde przechwycone
połączenie.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -std=c++11" \
	%{!?with_cairo:--enable-cairo=false}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md TODO.txt
%attr(755,root,root) %{_bindir}/tcpflow
%{_mandir}/man1/tcpflow.1*
