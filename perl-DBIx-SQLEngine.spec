#
# Conditional build:
# _with_tests - perform "make test" (requires working DBI connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	SQLEngine
Summary:	DBIx::SQLEngine - Extends DBI with high-level operations
Summary(pl):	DBIx::SQLEngine - rozszerzenie DBI o wysokopoziomowe operacje
Name:		perl-DBIx-SQLEngine
Version:	0.009
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl-DBI >= 1.0
BuildRequires:	perl-DBIx-AnyDBD >= 2.0
BuildRequires:	perl-Class-MakeMethods >= 1.003
BuildRequires:	perl-Class-MakeMethods-Template >= 1.003
%endif
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/DBIx/*.pm
%dir %{perl_vendorlib}/DBIx/SQLEngine
%{perl_vendorlib}/DBIx/SQLEngine/*.pm
%{perl_vendorlib}/DBIx/SQLEngine/Criteria
%{perl_vendorlib}/DBIx/SQLEngine/Mixin
%{_mandir}/man3/*
