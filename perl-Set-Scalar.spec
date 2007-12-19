#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Scalar
Summary:	Set::Scalar - basic set operations
Summary(pl.UTF-8):	Set::Scalar - podstawowe operacje na zbiorach
Name:		perl-Set-Scalar
Version:	1.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Set/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28906c7f21874e4746f36cb544d885a1
URL:		http://search.cpan.org/dist/Set-Scalar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Scalar - basic set operations.

%description -l pl.UTF-8
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
%{perl_vendorlib}/Set/*.pm
%{perl_vendorlib}/Set/Scalar
%{_mandir}/man3/*
