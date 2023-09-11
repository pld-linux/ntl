Summary:	Numbert Theory Library
Summary(pl.UTF-8):	Biblioteka do teorii liczb
Name:		ntl
Version:	11.5.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://libntl.org/%{name}-%{version}.tar.gz
# Source0-md5:	abd887865df30c02609210a86cb953b1
URL:		https://libntl.org/
BuildRequires:	gmp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NTL is a high-performance, portable C++ library providing data
structures and algorithms for arbitrary length integers; for vectors,
matrices, and polynomials over the integers and over finite fields;
and for arbitrary precision floating point arithmetic.

%description -l pl.UTF-8
NTL to wydajna, przenośna biblioteka C++ udostępniająca struktury
danych i algorytmy dla liczb całkowitych dowolnej długości; dla
wektorów, macierzy, wielomianów w przestrzeni liczb całkowitych i
ciałach skończonych; oraz dla liczb zmiennoprzecinkowych dowolnej
dokładności.

%package devel
Summary:	Header files for NTL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki NTL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel
Requires:	libstdc++-devel

%description devel
Header files for NTL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki NTL.

%package static
Summary:	Static NTL library
Summary(pl.UTF-8):	Statyczna biblioteka NTL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static NTL library.

%description static -l pl.UTF-8
Statyczna biblioteka NTL.

%package apidocs
Summary:	API documentation for NTL library
Summary(pl.UTF-8):	Dokumentacja API biblioteki NTL
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for NTL library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki NTL.

%prep
%setup -q

%build
cd src
./configure \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	NATIVE=off \
	SHARED=on

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_libdir}/libntl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntl.so.44

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntl.so
%{_libdir}/libntl.la
%{_includedir}/NTL

%files static
%defattr(644,root,root,755)
%{_libdir}/libntl.a

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/NTL
