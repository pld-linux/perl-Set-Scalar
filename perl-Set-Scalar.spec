
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	Scalar
Summary:	Set::Scalar - basic set operations
Summary(pl):	Set::Scalar - podstawowe operacje na zbiorach
Name:		perl-Set-Scalar
Version:	1.19
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6ad1793cb4eb8839efadb12b67e35364
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Scalar - basic set operations.

%description -l pl
Set::Scalar - podstawowe operacje na zbiorach.

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
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
