Summary:	Linux Audio Developer's Configuration and Connection API
Summary(pl):	Biblioteka LADCCA (Linux Audio Developer's Configuration and Connection API)
Name:		ladcca
Version:	0.4.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://lash-audio-session-handler.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	ffaff8a1ef560eb14bed3eb684ca4159
Patch0:		%{name}-compile.patch
URL:		http://lash-audio-session-handler.org/
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.50.0
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tetex
Requires(post,postun):	/sbin/ldconfig
Requires(post):	grep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LADCCA is a session management system for JACK and ALSA audio
applications on Linux.

%description -l pl
LADCCA jest zarz±dc± sesji dla JACK-a i ALSA oraz opartych o nie
programów dla Linuksa.

%package devel
Summary:	Development files for LADCCA
Summary(pl):	Pliki nag³ówkowe biblioteki LADCCA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuuid-devel
Obsoletes:	ladcca-docs

%description devel
This package contains header files for the LADCCA library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki LADCCA.

%package static
Summary:	Static LADCCA library
Summary(pl):	Statyczna wersja biblioteki LADCCA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static LADCCA library.

%description static -l pl
Ten pakiet zawiera bibliotekê statyczn± LADCCA.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--disable-serv-inst
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

if ! grep -q ^ladcca /etc/services; then
	echo -e "\nladcca\t\t14541/tcp\t\t\t# LADCCA client/server protocol" >> /etc/services
fi

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ladcca*
%attr(755,root,root) %{_libdir}/libladcca.so.*.*
%{_datadir}/ladcca
%{_infodir}/ladcca-manual*

%files devel
%defattr(644,root,root,755)
%doc docs/{api-proposal.html,*-split/*.html}
%attr(755,root,root) %{_libdir}/libladcca.so
%{_libdir}/libladcca.la
%{_includedir}/ladcca-1.0
%{_pkgconfigdir}/ladcca-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libladcca.a
