#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	SQLEngine
Summary:	DBIx::SQLEngine - Extends DBI with high-level operations
Summary(pl):	DBIx::SQLEngine - rozszerzenie DBI o wysokopoziomowe operacje
Name:		perl-DBIx-SQLEngine
Version:	0.007
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBIx::SQLEngine class provides an extended interface for the DBI
database interface, adding methods that support ad-hoc SQL generation
and query execution in a single call.

%description -l pl
Klasa DBIx::SQLEngine udostêpnia rozszerzony interfejs dla interfejsu
bazodanowego DBI, dodaj±c metody obs³uguj±ce generowanie SQL w locie
i wykonywanie zapytañ w pojedynczym wywo³aniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/DBIx/*.pm
%dir %{perl_sitelib}/DBIx/SQLEngine
%{perl_sitelib}/DBIx/SQLEngine/*.pm
%{perl_sitelib}/DBIx/SQLEngine/Criteria
%{perl_sitelib}/DBIx/SQLEngine/Mixin
%{_mandir}/man3/*
