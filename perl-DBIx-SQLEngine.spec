#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working DBI connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	SQLEngine
Summary:	DBIx::SQLEngine - Extends DBI with high-level operations
Summary(pl):	DBIx::SQLEngine - rozszerzenie DBI o wysokopoziomowe operacje
Name:		perl-DBIx-SQLEngine
Version:	0.010
%define		_ver 0.01
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	acc00692ef771ac9ab1ea7c823cd8ac5
BuildRequires:	perl-devel >= 5.6
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
%setup -q -n %{pdir}-%{pnam}-%{_ver}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

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
