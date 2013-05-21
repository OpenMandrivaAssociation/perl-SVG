%define upstream_name SVG
%define upstream_version 2.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for generating Scalable Vector Graphics (SVG) documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVG/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
SVG is a Perl module which generates a nested data structure containing the
DOM representation of an SVG (Scalable Vector Graphics) image. Using SVG, you
can generate SVG objects, embed other SVG instances into it, access the DOM
object, create and access javascript, and generate SMIL animation content.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl -pi -e 's/\cM//' examples/*.{pl,cgi}
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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.500.0-4mdv2012.0
+ Revision: 765666
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.500.0-3
+ Revision: 764177
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.500.0-2
+ Revision: 667305
- mass rebuild

* Fri Apr 09 2010 Jérôme Quelin <jquelin@mandriva.org> 2.500.0-1mdv2011.0
+ Revision: 533392
- update to 2.50

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.490.0-1mdv2010.0
+ Revision: 404424
- rebuild using %%perl_convert_version

* Sat Jan 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.49-1mdv2009.1
+ Revision: 333265
- update to new version 2.49

* Mon Jan 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.48-1mdv2009.1
+ Revision: 328530
- update to new version 2.48

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.47-1mdv2009.1
+ Revision: 315120
- update to new version 2.47

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.44-2mdv2009.0
+ Revision: 265435
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.44-1mdv2009.0
+ Revision: 196479
- update to new version 2.44

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.42-1mdv2009.0
+ Revision: 196167
- update to new version 2.42
- update to new version 2.41

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.40-1mdv2009.0
+ Revision: 193927
- update to new version 2.40

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.37-1mdv2008.1
+ Revision: 177895
- update to new version 2.37

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.36-1mdv2008.1
+ Revision: 97565
- update to new version 2.36

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.34-1mdv2008.0
+ Revision: 65331
- new version

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.33-4mdv2008.0
+ Revision: 47034
- rebuild


* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.33-3mdv2007.0
- spec cleanup
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.33-2mdk 
- spec cleanup
- don't ship useless empty directories
- make test in %%check

* Tue May 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.33-1mdk
- 2.33
- Fix line endings in examples

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.32-2mdk
- fix buildrequires in a backward compatible way

* Tue Oct 19 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.32-1mdk
- 2.32
- Add examples

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.28-2mdk
- rpmbuildupdate aware

* Sun Jan 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.28-1mdk
- first mdk release

