Name:       audio-hal-ak4953
Summary:    TIZEN Audio HAL for AK4953
Version:    0.2.17
Release:    0
Group:      System/Libraries
License:    Apache-2.0
URL:        http://tizen.org
Source0:    audio-hal-ak4953-%{version}.tar.gz
BuildRequires: pkgconfig(vconf)
BuildRequires: pkgconfig(iniparser)
BuildRequires: pkgconfig(dlog)
BuildRequires: pkgconfig(alsa)
#BuildRequires: pkgconfig(tinyalsa)
Provides: libtizen-audio.so

%description
TIZEN Audio HAL for AK4953

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="$CFLAGS -DTIZEN_DEBUG_ENABLE -DSYSCONFDIR=\\\"%{_sysconfdir}\\\""
export CXXFLAGS="$CXXFLAGS -DTIZEN_DEBUG_ENABLE"
export FFLAGS="$FFLAGS -DTIZEN_DEBUG_ENABLE"

export USE_TINYALSA="0"

%autogen
%configure

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/license
cp LICENSE.Apache-2.0 %{buildroot}%{_datadir}/license/%{name}
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest audio-hal-ak4953.manifest
%defattr(-,root,root,-)
%{_libdir}/libtizen-audio.so
%{_datadir}/license/%{name}