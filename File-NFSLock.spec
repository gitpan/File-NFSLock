# Automatically generated by File-NFSLock.spec.PL
%define class File
%define subclass NFSLock
%define version 1.27
%define release 1
%define defperlver 5.6.1

# Derived values
%define real_name %{class}-%{subclass}
%define name perl-%{real_name}
%define perlver %(rpm -q perl --queryformat '%%{version}' 2> /dev/null || echo %{defperlver})

# Provide perl-specific find-{provides,requires}.
%define __find_provides %( echo -n /usr/lib/rpm/find-provides && [ -x /usr/lib/rpm/find-provides.perl ] && echo .perl )
%define __find_requires %( echo -n /usr/lib/rpm/find-requires && [ -x /usr/lib/rpm/find-requires.perl ] && echo .perl )

Summary:        Perl module %{class}::%{subclass}
Name:           %{name}
Version:        %{version}
Release:        %{release}
Group:          Development/Perl
License:        Artistic
Source:         http://www.cpan.org./modules/by-module/%{class}/%{real_name}-%{version}.tar.gz
URL:            http://search.cpan.org/search?dist=%{real_name}
Vendor:         Rob Brown <bbb@cpan.org>
Packager:       Rob Brown <bbb@cpan.org>
BuildRequires:  perl
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot-%(id -u -n)
Requires:       perl = %{perlver}
Provides:       %{real_name} = %{version}

%description
%{class}::%{subclass} Perl Module

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} PREFIX=$RPM_BUILD_ROOT%{_prefix}
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress
# Clean up some files we don't want/need
rm -rf `find $RPM_BUILD_ROOT -name "perllocal.pod" -o -name ".packlist" -o -name "*.bs"`
find $RPM_BUILD_ROOT%{_prefix} -type d | tac | xargs rmdir --ign

%clean
rm -rf $RPM_BUILD_ROOT
HERE=`pwd`
cd ..
rm -rf $HERE

%files
%defattr(-,root,root)
%doc README Changes examples
%{_prefix}

%changelog
* Thu May 30 2002 Rob Brown <bbb@cpan.org>
- initial creation
