#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	WWW
%define	pnam	Google-PageRank
Summary:	WWW::Google::PageRank - Query Google pagerank of page
Summary(pl.UTF-8):	WWW::Google::PageRank - zapytanie o ranking strony w Google
Name:		perl-WWW-Google-PageRank
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16437cb7f0f12c3b8529600a93140f38
URL:		http://search.cpan.org/dist/WWW-Google-PageRank/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The WWW::Google::PageRank is a class implementing a interface for
querying Google pagerank.

To use it, you should create WWW::Google::PageRank object and use
its method get(), to query page rank of URL.

It uses LWP::UserAgent for making request to Google.

%description -l pl.UTF-8
WWW::Google::PageRank to klasa implementująca interfejs do odpytywania
Google o ranking strony.

Aby go użyć, należy utworzyć obiekt WWW::Google::PageRank i użyć jego
metody get() do zapytania o ranking strony o podanym URL-u.

Klasa używa LWP::UserAgent do wykonywania zapytań do serwisu Google.

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
%doc Changes README
%{perl_vendorlib}/WWW/Google/*.pm
%{_mandir}/man3/*
