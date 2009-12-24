%define upstream_name    CPAN-Inject
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Base class for injecting distributions into CPAN sources
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN)
BuildRequires: perl(CPAN::Checksums)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Remove)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::chmod)
BuildRequires: perl(File::stat)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Script)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Following the release of the CPAN::Mini manpage, the the CPAN::Mini::Inject
manpage module was created to add additional distributions into a minicpan
mirror.

While it was created for use with a minicpan mirror, similar functionality
can be reused in other situations.

*CPAN::Inject* replicates the basics of this functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/cpaninject
/usr/share/man/man1/cpaninject.1.lzma

