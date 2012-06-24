#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unicode
%define		pnam	Map8
Summary:	Unicode::Map8 perl module 
Summary(cs):	Modul Unicode::Map8 pro Perl
Summary(da):	Perlmodul Unicode::Map8
Summary(de):	Unicode::Map8 Perl Modul
Summary(es):	M�dulo de Perl Unicode::Map8
Summary(fr):	Module Perl Unicode::Map8
Summary(it):	Modulo di Perl Unicode::Map8
Summary(ja):	Unicode::Map8 Perl �⥸�塼��
Summary(ko):	Unicode::Map8 �� ����
Summary(no):	Perlmodul Unicode::Map8
Summary(pl):	Modu� perla Unicode::Map8
Summary(pt_BR):	M�dulo Perl Unicode::Map8
Summary(pt):	M�dulo de Perl Unicode::Map8
Summary(ru):	������ ��� Perl Unicode::Map8
Summary(sv):	Unicode::Map8 Perlmodul
Summary(uk):	������ ��� Perl Unicode::Map8
Summary(zh_CN):	Unicode::Map8 Perl ģ��
Name:		perl-Unicode-Map8
Version:	0.11
Release:	5
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
Unicode::Map8 - tablice mapowania pomi�dzy 8-bitowymi znakami a
Unicodem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install {diff_iso,make*maps,map8_*,umap} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *txt
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/Unicode/Map8.pm
%{perl_sitearch}/Unicode/Map8
%dir %{perl_sitearch}/auto/Unicode/Map8
%{perl_sitearch}/auto/Unicode/Map8/Map8.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/Map8/Map8.so
%{_mandir}/man[13]/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
