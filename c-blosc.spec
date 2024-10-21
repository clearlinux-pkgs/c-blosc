#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: a19cdc7
#
Name     : c-blosc
Version  : 1.21.6
Release  : 1
URL      : https://github.com/Blosc/c-blosc/archive/refs/tags/v1.21.6.tar.gz
Source0  : https://github.com/Blosc/c-blosc/archive/refs/tags/v1.21.6.tar.gz
Summary  : A blocking, shuffling and lossless compression library
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 MIT Zlib
Requires: c-blosc-lib = %{version}-%{release}
Requires: c-blosc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : snappy-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ZLIB DATA COMPRESSION LIBRARY
zlib 1.3.1 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://tools.ietf.org/html/rfc1950 (zlib format), rfc1951 (deflate format) and
rfc1952 (gzip format).

%package dev
Summary: dev components for the c-blosc package.
Group: Development
Requires: c-blosc-lib = %{version}-%{release}
Provides: c-blosc-devel = %{version}-%{release}
Requires: c-blosc = %{version}-%{release}

%description dev
dev components for the c-blosc package.


%package lib
Summary: lib components for the c-blosc package.
Group: Libraries
Requires: c-blosc-license = %{version}-%{release}

%description lib
lib components for the c-blosc package.


%package license
Summary: license components for the c-blosc package.
Group: Default

%description license
license components for the c-blosc package.


%prep
%setup -q -n c-blosc-1.21.6
cd %{_builddir}/c-blosc-1.21.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729493722
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1729493722
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/c-blosc
cp %{_builddir}/c-blosc-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/c-blosc/f95d3411831b0a3233ecbba99b85d2f1688773cd || :
cp %{_builddir}/c-blosc-%{version}/LICENSES/BITSHUFFLE.txt %{buildroot}/usr/share/package-licenses/c-blosc/d1b152dfd8ac42778f5d4aacfb62b92bf2ab4145 || :
cp %{_builddir}/c-blosc-%{version}/LICENSES/FASTLZ.txt %{buildroot}/usr/share/package-licenses/c-blosc/7f9f00bd71460bbd6551c361fe5e95023ab69ebd || :
cp %{_builddir}/c-blosc-%{version}/LICENSES/SNAPPY.txt %{buildroot}/usr/share/package-licenses/c-blosc/0d45aa696e5c82d8d1a1a1bbdc55d8e5fc328ccc || :
cp %{_builddir}/c-blosc-%{version}/LICENSES/STDINT.txt %{buildroot}/usr/share/package-licenses/c-blosc/257fcfb59f520ac78cf01eb575d07aacfbb41b37 || :
cp %{_builddir}/c-blosc-%{version}/LICENSES/ZLIB.txt %{buildroot}/usr/share/package-licenses/c-blosc/233f44af3fb55dcc7fddfef8e77ac627b0008756 || :
cp %{_builddir}/c-blosc-%{version}/internal-complibs/zlib-1.3.1/LICENSE %{buildroot}/usr/share/package-licenses/c-blosc/233f44af3fb55dcc7fddfef8e77ac627b0008756 || :
cp %{_builddir}/c-blosc-%{version}/internal-complibs/zlib-1.3.1/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/c-blosc/3f317fbb3e08fd99169d2e77105d562ea0e482c7 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/blosc-export.h
/usr/include/blosc.h
/usr/lib64/libblosc.so
/usr/lib64/pkgconfig/blosc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libblosc.so.1
/usr/lib64/libblosc.so.1.21.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/c-blosc/0d45aa696e5c82d8d1a1a1bbdc55d8e5fc328ccc
/usr/share/package-licenses/c-blosc/233f44af3fb55dcc7fddfef8e77ac627b0008756
/usr/share/package-licenses/c-blosc/257fcfb59f520ac78cf01eb575d07aacfbb41b37
/usr/share/package-licenses/c-blosc/3f317fbb3e08fd99169d2e77105d562ea0e482c7
/usr/share/package-licenses/c-blosc/7f9f00bd71460bbd6551c361fe5e95023ab69ebd
/usr/share/package-licenses/c-blosc/d1b152dfd8ac42778f5d4aacfb62b92bf2ab4145
/usr/share/package-licenses/c-blosc/f95d3411831b0a3233ecbba99b85d2f1688773cd