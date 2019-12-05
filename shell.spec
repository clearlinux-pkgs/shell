#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : shell
Version  : 1.0.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/71/0c/d6270ed3bf86d036c37929443d7f4a7a8af77dbbce11cec7ddce8d8599c5/shell-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/71/0c/d6270ed3bf86d036c37929443d7f4a7a8af77dbbce11cec7ddce8d8599c5/shell-1.0.1.tar.gz
Summary  : A better way to run shell commands in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: shell-python3
Requires: shell-license
Requires: shell-python
BuildRequires : buildreq-distutils3

%description
shell
        =====
        
        """A better way to run shell commands in Python."""
        
        Built because every time I go to use `subprocess`_, I spend more time in the
        docs & futzing around than actually implementing what I'm trying to get done.

%package license
Summary: license components for the shell package.
Group: Default

%description license
license components for the shell package.


%package python
Summary: python components for the shell package.
Group: Default
Requires: shell-python3 = %{version}-%{release}

%description python
python components for the shell package.


%package python3
Summary: python3 components for the shell package.
Group: Default
Requires: python3-core

%description python3
python3 components for the shell package.


%prep
%setup -q -n shell-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539122077
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/shell
cp LICENSE %{buildroot}/usr/share/doc/shell/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/shell/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
