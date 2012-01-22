%define upstream_name	 SVG
%define upstream_version 2.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl extension for generating Scalable Vector Graphics (SVG) documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVG/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
SVG is a Perl module which generates a nested data structure containing the
DOM representation of an SVG (Scalable Vector Graphics) image. Using SVG, you
can generate SVG objects, embed other SVG instances into it, access the DOM
object, create and access javascript, and generate SMIL animation content.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl -pi -e 's/\cM//' examples/*.{pl,cgi}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes examples
%{perl_vendorlib}/SVG
%{perl_vendorlib}/SVG.pm
%{_mandir}/*/*
