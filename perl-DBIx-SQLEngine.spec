#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working DBI connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	SQLEngine
Summary:	DBIx::SQLEngine - extends DBI with high-level operations
Summary(pl):	DBIx::SQLEngine - rozszerzenie DBI o wysokopoziomowe operacje
Name:		perl-DBIx-SQLEngine
Version:	0.93
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	963f4e41b77f7a1f6287eeac760a94e1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/DBIx/*.pm
%dir %{perl_vendorlib}/DBIx/SQLEngine
%{perl_vendorlib}/DBIx/SQLEngine/*.pm
%{perl_vendorlib}/DBIx/SQLEngine/Cache
%{perl_vendorlib}/DBIx/SQLEngine/Criteria
%{perl_vendorlib}/DBIx/SQLEngine/Driver
%{perl_vendorlib}/DBIx/SQLEngine/Record
%{perl_vendorlib}/DBIx/SQLEngine/RecordSet
%{perl_vendorlib}/DBIx/SQLEngine/Schema
%{perl_vendorlib}/DBIx/SQLEngine/Utility
%{_mandir}/man3/*
