#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django_compressor
Version  : 2.2
Release  : 27
URL      : https://files.pythonhosted.org/packages/82/76/1355459f90714517c52f264aa7245b52e59a273ec16e8f8d505fa6c342f8/django_compressor-2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/82/76/1355459f90714517c52f264aa7245b52e59a273ec16e8f8d505fa6c342f8/django_compressor-2.2.tar.gz
Summary  : Compresses linked and inline JavaScript or CSS into single cached files.
Group    : Development/Tools
License  : MIT NCSA
Requires: django_compressor-python3
Requires: django_compressor-license
Requires: django_compressor-python
Requires: django-appconf
Requires: rcssmin
Requires: rjsmin
BuildRequires : buildreq-distutils3
BuildRequires : django-appconf
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : rcssmin
BuildRequires : rjsmin
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
=================

%package license
Summary: license components for the django_compressor package.
Group: Default

%description license
license components for the django_compressor package.


%package python
Summary: python components for the django_compressor package.
Group: Default
Requires: django_compressor-python3

%description python
python components for the django_compressor package.


%package python3
Summary: python3 components for the django_compressor package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django_compressor package.


%prep
%setup -q -n django_compressor-2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532325986
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/django_compressor
cp LICENSE %{buildroot}/usr/share/doc/django_compressor/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/django_compressor/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
