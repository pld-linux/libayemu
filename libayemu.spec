Summary:	The AY/YM sound chip emulator library
Summary(pl.UTF-8):   Biblioteka emulująca układ dźwiękowy AY/YM
Name:		libayemu
Version:	0.9.5
Release:	1
# specified in <ayemu.h>
License:	LGPL v2+
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libayemu/%{name}-%{version}.tar.gz
# Source0-md5:	aedf8c562b3e47584bf42114a438b6ed
Patch0:		%{name}-am.patch
URL:		http://sashnov.nm.ru/libayemu.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the AY/YM sound chip emulator. This chip was used in wide
range of old popular machines as Sinclair ZX Spectrum 128, Amstrad,
Atari ST and others. With this library you can hear music from these
computers games or add AY/YM music to your own games/demoz/etc.

%description -l pl.UTF-8
Bibliotela emulująca układ dźwiękowy AY/YM. Układ ten był używany w
wielu starych popularnych komputerach takich jak ZX Spectrum 128,
Amstrad, Atari ST i innych. Używając tej biblioteki można słuchać
muzyki z gier produkowanych na te komputery. Można również użyć plików
muzycznych dla układu AY/YM w swoich własnych grach, demach itp.

%package devel
Summary:	Header files for libayemu library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libayemu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libayemu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libayemu.

%package static
Summary:	Static libayemu library
Summary(pl.UTF-8):   Statyczna biblioteka libayemu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libayemy library.

%description static -l pl.UTF-8
Statyczna biblioteka libayemu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
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
%doc AUTHORS ChangeLog README RELEASENOTES THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
