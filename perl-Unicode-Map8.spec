#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	Map8
Summary:	Unicode::Map8 - mapping table between 8-bit chars and Unicode
Summary(pl):	Unicode::Map8 - tabela odwzorowuj±ca miêdzy znakami 8-bitowymi a Unikodem
Name:		perl-Unicode-Map8
Version:	0.12
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b76a10615258894b1699b140f93940d0
Patch0:		%{name}-types.patch
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Unicode::Map8 class implement efficient mapping tables between
8-bit character sets and 16 bit character sets like Unicode. The
tables are efficient both in terms of space allocated and translation
speed. The 16-bit strings is assumed to use network byte order.

%description -l pl
Klasa Unicode::Map8 implementuje wydajne tablice odwzorowuj±ce
pomiêdzy 8-bitowymi zestawami znaków a 16-bitowymi zestawami takimi
jak Unikod. Tablice s± wydajne zarówno je¶li chodzi o ilo¶æ
przydzielonego miejsca, jak i szybko¶æ konwersji. Zak³ada siê, ¿e
³añcuchy 16-bitowe u¿ywaj± sieciowej kolejno¶ci bajtów w s³owie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install {diff_iso,make*maps,map8_*,umap} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *txt
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Unicode/Map8.pm
%{perl_vendorarch}/Unicode/Map8
%dir %{perl_vendorarch}/auto/Unicode/Map8
%{perl_vendorarch}/auto/Unicode/Map8/Map8.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/Map8/Map8.so
%{_mandir}/man[13]/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
