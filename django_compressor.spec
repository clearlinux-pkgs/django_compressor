#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django_compressor
Version  : 2.3
Release  : 31
URL      : https://files.pythonhosted.org/packages/73/ba/e14cc0a8ebecb043175abee1dcab15b2612952f91793ddfdfeefd0892a2f/django_compressor-2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/73/ba/e14cc0a8ebecb043175abee1dcab15b2612952f91793ddfdfeefd0892a2f/django_compressor-2.3.tar.gz
Summary  : Compresses linked and inline JavaScript or CSS into single cached files.
Group    : Development/Tools
License  : MIT NCSA
Requires: django_compressor-license = %{version}-%{release}
Requires: django_compressor-python = %{version}-%{release}
Requires: django_compressor-python3 = %{version}-%{release}
Requires: django-appconf
Requires: rcssmin
Requires: rjsmin
BuildRequires : buildreq-distutils3
BuildRequires : django-appconf
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : rcssmin
BuildRequires : rjsmin
BuildRequires : tox
BuildRequires : virtualenv

%description
Django Compressor
=================
.. image:: https://codecov.io/github/django-compressor/django-compressor/coverage.svg?branch=develop
:target: https://codecov.io/github/django-compressor/django-compressor?branch=develop

%package license
Summary: license components for the django_compressor package.
Group: Default

%description license
license components for the django_compressor package.


%package python
Summary: python components for the django_compressor package.
Group: Default
Requires: django_compressor-python3 = %{version}-%{release}

%description python
python components for the django_compressor package.


%package python3
Summary: python3 components for the django_compressor package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django_compressor package.


%prep
%setup -q -n django_compressor-2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559273730
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django_compressor
cp LICENSE %{buildroot}/usr/share/package-licenses/django_compressor/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django_compressor/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
