Summary:	TCP Flow Recorder
Summary(pl):	Program zapisuj±cy ruch TCP
Name:		tcpflow
Version:	0.21
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.circlemud.org/pub/jelson/tcpflow/%{name}-%{version}.tar.gz
# Source0-md5:	45a5aef6f043312315b7f342afc4a9c5
URL:		http://www.circlemud.org/~jelson/software/tcpflow/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpflow is program that captures data transmitted as part of TCP
connections, and and stores the data in a way that is convenient
for protocol analysis or debugging. Tcpflow stores all captured
data in two files per connection.

%description -l pl
Tcpflow jest programem, który przechwytuje dane przesy³ane w ramach
po³±czeñ TCP i zapisuje je w sposób wygodny do analizy lub ¶ledzenia
protoko³u - tworz±c dwa pliki z danymi na ka¿de przechwycone
po³±czenie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
