#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-JHash
Version  : 0.10
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-0.10.tar.gz
Summary  : 'Perl extension for 32 bit Jenkins Hashing Algorithm'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Digest-JHash-lib
Requires: perl-Digest-JHash-man

%description
Digest/JHash version 0.03
=========================
INSTALLATION
To install this module type the following (nmake on Win32):

%package lib
Summary: lib components for the perl-Digest-JHash package.
Group: Libraries

%description lib
lib components for the perl-Digest-JHash package.


%package man
Summary: man components for the perl-Digest-JHash package.
Group: Default

%description man
man components for the perl-Digest-JHash package.


%prep
%setup -q -n Digest-JHash-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Digest/JHash.pm

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Digest/JHash/JHash.so

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Digest::JHash.3
