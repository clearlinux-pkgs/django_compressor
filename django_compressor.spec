#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django_compressor
Version  : 2.1
Release  : 19
URL      : http://pypi.debian.net/django_compressor/django_compressor-2.1.tar.gz
Source0  : http://pypi.debian.net/django_compressor/django_compressor-2.1.tar.gz
Summary  : Compresses linked and inline JavaScript or CSS into single cached files.
Group    : Development/Tools
License  : MIT NCSA
Requires: django_compressor-python
BuildRequires : django-appconf 
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : rcssmin 
BuildRequires : rjsmin 
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Django Compressor
=================
.. image:: https://codecov.io/github/django-compressor/django-compressor/coverage.svg?branch=develop
:target: https://codecov.io/github/django-compressor/django-compressor?branch=develop

%package python
Summary: python components for the django_compressor package.
Group: Default

%description python
python components for the django_compressor package.


%prep
%setup -q -n django_compressor-2.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
