%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	Map8
Summary:	Unicode::Map8 perl module
Summary(pl):	Modu³ perla Unicode::Map8
Name:		perl-Unicode-Map8
Version:	0.11
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Unicode-String
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::Map8 - Mapping table between 8-bit chars and Unicode.

%description -l pl
Unicode::Map8 - tablice mapowania pomiêdzy 8-bitowymi znakami a
Unicodem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install {diff_iso,make*maps,map8_*,umap} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Unicode/Map8.pm
%{perl_sitearch}/Unicode/Map8
%dir %{perl_sitearch}/auto/Unicode/Map8
%{perl_sitearch}/auto/Unicode/Map8/Map8.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/Map8/Map8.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
