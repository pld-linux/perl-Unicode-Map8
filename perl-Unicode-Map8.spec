%include	/usr/lib/rpm/macros.perl
Summary:	Unicode-Map8 perl module
Summary(pl):	Modu³ perla Unicode-Map8
Name:		perl-Unicode-Map8
Version:	0.06
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/Unicode-Map8-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Unicode-String
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Unicode-Map8 - Mapping table between 8-bit chars and Unicode.

%description -l pl
Unicode-Map8 - tablice mapowania pomiêdzy 8-bitowymi znakami a Unicodem.

%prep
%setup -q -n Unicode-Map8-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install {diff_iso,make*maps,map8_*,umap} \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Unicode/Map8/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Unicode/Map8
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,rfc1345.txt}.gz

%{perl_sitearch}/Unicode/Map8.pm
%{perl_sitearch}/Unicode/Map8

%dir %{perl_sitearch}/auto/Unicode/Map8
%{perl_sitearch}/auto/Unicode/Map8/.packlist
%{perl_sitearch}/auto/Unicode/Map8/Map8.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/Map8/Map8.so

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
