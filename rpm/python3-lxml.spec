# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-lxml
Summary:    ElementTree-like Python bindings for libxml2 and libxslt
Version:    5.5.0
Release:    1
License:    BSD
URL:        http://lxml.de/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  python3-cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.


%prep
%setup -q -n %{name}-%{version}/lxml

%build
CFLAGS="%{optflags}" %{__python3} setup.py build %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSES.txt
%doc README.rst CREDITS.txt CHANGES.txt doc/
%{python3_sitearch}/*
