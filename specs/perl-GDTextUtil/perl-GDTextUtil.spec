# $Id$
# Authority: dag
# Upstream: Martien Verbruggen <mverb$cpan,org>

### EL6 ships with perl-GDTextUtil-0.86-15.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GDTextUtil

Summary: Text utilities for use with GD
Name: perl-GDTextUtil
Version: 0.86
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GDTextUtil/

Source: http://www.cpan.org/authors/id/M/MV/MVERB/GDTextUtil-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Text utilities for use with GD.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/GD::Text.3pm*
%doc %{_mandir}/man3/GD::Text::*.3pm*
%dir %{perl_vendorlib}/GD/
%{perl_vendorlib}/GD/Text/
%{perl_vendorlib}/GD/Text.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.86-1
- Initial package. (using DAR)
