Summary:	Linux Audio Developer's Configuration and Connection API
Summary(pl):	Biblioteka LADCCA (Linux Audio Developer's Configuration and Connection API)
Name:		ladcca
Version:	0.3.1
Release:	3
License:	GPL
Group:		Applications/Multimedia
Source0:	http://pkl.net/~node/software/%{name}-%{version}.tar.gz
# Source0-md5: a3f0c1eab6c3dc852dca46e1e4c1a8f7
Patch0:		%{name}-compile.patch
Patch1:		%{name}-include.patch
URL:		http://pkl.net/~node/ladcca.html/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libuuid-devel
BuildRequires:	readline-devel
BuildRequires:	tetex
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LADCCA is a session management system for JACK and ALSA audio
applications on Linux.

%description -l pl
LADCCA jest zarządcą sesji dla JACKa i ALSA oraz opartych o nie
programów dla Linuksa.

%package devel
Summary:	Development files for LADCCA
Summary(pl):	Pliki nagłówkowe biblioteki LADCCA
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libuuid-devel
Obsoletes:	ladcca-docs

%description devel
This package contains header files for the LADCCA library.

%description devel -l pl
Ten pakiet zawiera pliki nagłówkowe biblioteki LADCCA.

%package static
Summary:	Static LADCCA library
Summary(pl):	Statyczna wersja biblioteki LADCCA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static LADCCA library.

%description static -l pl
Ten pakiet zawiera bibliotekę statyczną LADCCA.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-default-dir="~/audio_project"
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

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ladcca*
%attr(755,root,root) %{_libdir}/libladcca.so.*.*
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
