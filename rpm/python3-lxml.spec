Name:       python3-lxml
Summary:    ElementTree-like Python bindings for libxml2 and libxslt
Version:    4.6.5
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

%package doc
Summary: Documentation for Python bindings for libxml2 and libxslt

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/lxml

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%license LICENSES.txt
%{python3_sitearch}/*

%files doc
%defattr(-,root,root,-)
%doc README.rst CREDITS.txt CHANGES.txt doc/
