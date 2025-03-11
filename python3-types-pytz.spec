Summary:	Typing stubs for pytz
Summary(pl.UTF-8):	Zaślepki typów dla modułu pytz
Name:		python3-types-pytz
Version:	2023.3.0.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/types-pytz/
Source0:	https://files.pythonhosted.org/packages/source/t/types-pytz/types-pytz-%{version}.tar.gz
# Source0-md5:	7da1b15fe5da383f134eb59e64324ffa
URL:		https://pypi.org/project/types-pytz/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEP 561 type stub package for the pytz package. It can be
used by type-checking tools like mypy, pyright, pytype, PyCharm, etc.
to check code that uses pytz.

%description -l pl.UTF-8
Ten pakiet zawiera zaślepki typów zgodne z PEP 561 dla pakietu pytz.
Mogą one być używany przez narzędzia sprawdzające typy, takie jak
mypy, pyright, pytype, PyCharm itp. do sprawdzania kodu
wykorzystującego pytz.

%prep
%setup -q -n types-pytz-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md 
%{py3_sitescriptdir}/pytz-stubs
%{py3_sitescriptdir}/types_pytz-%{version}-py*.egg-info
