%define modname	SVG
%define modver 2.59

Summary:	Perl extension for generating Scalable Vector Graphics (SVG) documents
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/SVG/SVG-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
SVG is a Perl module which generates a nested data structure containing the
DOM representation of an SVG (Scalable Vector Graphics) image. Using SVG, you
can generate SVG objects, embed other SVG instances into it, access the DOM
object, create and access javascript, and generate SMIL animation content.

%prep
%setup -qn %{modname}-%{modver}
perl -pi -e 's/\cM//' examples/*.{pl,cgi}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files 
%doc README Changes examples
%{perl_vendorlib}/SVG
%{perl_vendorlib}/SVG.pm
%{_mandir}/man3/*


