Summary:	Linux Audio Developer's Configuration and Connection API
Name:		ladcca
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://pkl.net/~node/software/%{name}-%{version}.tar.gz
Patch0:		%{name}-compile.patch
URL:		http://pkl.net/~node/ladcca.html/
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	readline-devel
BuildRequires:	XFree86-devel
BuildRequires:	gtk+2-devel
BuildRequires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LADCCA is a session management system for JACK and ALSA audio
applications on GNU/Linux.

%description -l pl
LADCCA jest zarz±dc± sesji dla JACKa i ALSA oraz opartych o nie
programów dla GNU/Linux.

%package	docs
Summary:	Documentation files for LADCCA
Summary(pl):	Dokumentacja dla LADCCA
Group:		Documentation
Requires:	%{name} = %{version}

%description	docs
This package contains documentation for LADDCA.

%description -l pl
Ten pakiet zawiera dokumentacje dla LADCCA.

%package	devel
Summary:	Development files for LADCCA
Summary(pl):	Pliki nag³ówkowe dla LADCCA
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description	devel
This package contains development libraries for the LADCCA library.

%description -l pl
Ten pakiet zawiera pliki nag³ówkowe dla LADCCA

%package	static
Summary:	Static LADCCA libraries.
Summary(pl):	Statyczne wersje bibliotek z LADCCA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for the LADCCA library.

%description -l pl
Ten pakiet zawiera biblioteki statyczne dla LADCCA

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-default-dir="~/audio_project"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/ladcca-manual-html-one-page
install -d $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/ladcca-manual-html-split
cp docs/ladcca-manual-html-one-page/*.html $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/ladcca-manual-html-one-page
cp docs/ladcca-manual-html-split/*.html $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/ladcca-manual-html-split
cp docs/*.html $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
cp docs/*.tex* $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
cp docs/ladcca-manual.texi $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/ladcca*
%attr(755,root,root) %{_libdir}/libladcca.so.1
%attr(755,root,root) %{_libdir}/libladcca.so.1.*
%{_datadir}/info/ladcca-manual*

%files docs
%defattr(644,root,root,755)
%dir %{_datadir}/doc
%dir %{_datadir}/doc/%{name}/ladcca-manual-html-one-page
%dir %{_datadir}/doc/%{name}/ladcca-manual-html-split
%{_datadir}/doc/%{name}/ladcca-manual-html-one-page/*.html
%{_datadir}/doc/%{name}/ladcca-manual-html-split/*.html
%{_datadir}/doc/%{name}/ladcca-manual.texi
%{_datadir}/doc/%{name}/api-proposal.html
%{_datadir}/doc/%{name}/fdl.texi
%{_datadir}/doc/%{name}/texinfo.tex

%files devel
%defattr(644,root,root,755)
%{_libdir}/pkgconfig/ladcca-1.0.pc
%{_libdir}/libladcca.la
%{_libdir}/libladcca.so
%{_includedir}/ladcca-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libladcca.a
