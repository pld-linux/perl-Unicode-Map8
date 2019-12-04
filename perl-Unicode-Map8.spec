#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unicode
%define		pnam	Map8
Summary:	Unicode::Map8 - mapping table between 8-bit chars and Unicode
Summary(pl.UTF-8):	Unicode::Map8 - tabela odwzorowująca między znakami 8-bitowymi a Unikodem
Name:		perl-Unicode-Map8
Version:	0.13
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc93a37cabcae488bd95ca07bf5c919e
Patch0:		%{name}-types.patch
URL:		http://search.cpan.org/dist/Unicode-Map8/
BuildRequires:	perl-Unicode-String >= 2.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Unicode::Map8 class implement efficient mapping tables between
8-bit character sets and 16 bit character sets like Unicode. The
tables are efficient both in terms of space allocated and translation
speed. The 16-bit strings is assumed to use network byte order.

%description -l pl.UTF-8
Klasa Unicode::Map8 implementuje wydajne tablice odwzorowujące
pomiędzy 8-bitowymi zestawami znaków a 16-bitowymi zestawami takimi
jak Unikod. Tablice są wydajne zarówno jeśli chodzi o ilość
przydzielonego miejsca, jak i szybkość konwersji. Zakłada się, że
łańcuchy 16-bitowe używają sieciowej kolejności bajtów w słowie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install {diff_iso,make*maps,map8_*} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README rfc1345.txt
%attr(755,root,root) %{_bindir}/umap
%{perl_vendorarch}/Unicode/Map8.pm
%{perl_vendorarch}/Unicode/Map8
%dir %{perl_vendorarch}/auto/Unicode/Map8
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/Map8/Map8.so
%{_mandir}/man1/umap.1p*
%{_mandir}/man3/Unicode::Map8.3pm*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
