Summary:	The AY/YM sound chip emulator library
Summary(pl):	Biblioteka emuluj±ca uk³ad d¼wiêkowy AY/YM
Name:		libayemu
Version:	0.9.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libayemu/%{name}-%{version}.tar.gz
# Source0-md5:	aedf8c562b3e47584bf42114a438b6ed
Patch0:		%{name}-am.patch
URL:		http://sashnov.nm.ru/libayemu.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the AY/YM sound chip emulator. This chip was used in wide
range of old popular machines as Sinclair ZX Spectrum 128, Amstrad,
Atari and others. With this library you can hear music from these
computers games or add AY/YM music to your own games/demoz/etc.

%description -l pl
Bibliotela emuluj±ca uk³ad d¼wiêkowy AY/YM. Uk³ad ten by³ u¿ywany w
wielu starych popularnych komputerach takich jak ZX Spectrum 128,
Amstrad, Atari i innych. U¿ywaj±c tej biblioteki mo¿na s³uchaæ
muzyki z gier produkowanych na te komputery. Mo¿na równie¿ u¿yæ plików
muzycznych dla uk³adu AY/YM w swoich w³asnych grach, demach itp.

%package devel
Summary:	Header files for libayemu library
Summary(pl):	Pliki nag³ówkowe biblioteki libayemu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libayemu library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libayemu.

%package static
Summary:	Static libayemu library
Summary(pl):	Statyczna biblioteka libayemu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libayemy library.

%description static -l pl
Statyczna biblioteka libayemu.

%prep
%setup -q
%patch0 -p1

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
