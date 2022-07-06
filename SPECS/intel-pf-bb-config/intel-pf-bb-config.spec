%global inih_version 44
Summary:       A tool for configuring certain Intel baseband devices
Name:          intel-pf-bb-config
Version:       21.11
Release:       1%{?dist}
License:       ASL 2.0
Vendor:        Microsoft
Distribution:  Mariner
Group:         System/Tools
URL:           https://github.com/intel/pf-bb-config
Source0:       https://github.com/benhoyt/inih/archive/r%{inih_version}.tar.gz#/inih-%{inih_version}.tar.gz
Source1:       https://github.com/intel/pf-bb-config/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make

%description
This application provides a means to configure certain Intel baseband devices by
accessing their configuration space and setting parameters via MMIO.

%prep
%setup -q -n inih-r%{inih_version}
%setup -q -T -D -b 1 -n pf-bb-config-%{version}

%build
# Build the INI parser library
pushd ../inih-r%{inih_version}/extra
make -f Makefile.static
cp libinih.a ..
popd

cd ..
export INIH_PATH=$PWD/inih-r%{inih_version}

# Build the baseband tool
pushd pf-bb-config-%{version}
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 pf_bb_config %{buildroot}%{_bindir}/pf_bb_config

%ldconfig_scriptlets

%files

%license LICENSE

%{_bindir}/pf_bb_config

%changelog
* Thu Feb 17 2022 Vince Perri <viperri@microsoft.com> - 21.11-1
- Original version for CBL-Mariner.
- License verified
