%global aname visualization.spectrum
%global kodi_version 17.0

Name:           kodi-visualization-spectrum
Version:        1.1.4
Release:        1%{?dist}
Summary:        Spectrum visualizer for Kodi
Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/xbmc/visualization.spectrum
Source0:        https://github.com/xbmc/%{aname}/archive/v%{version}/%{aname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  kodi-devel >= %{kodi_version}

Requires:       kodi >= %{kodi_version}

ExclusiveArch:  i686 x86_64

%description
%{summary}.

%prep
%setup -q -n %{aname}-%{version}

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.cpp' | xargs chmod a-x

# Patch incorrect fsf address
sed -i "s|59 Temple Place - Suite 330, Boston, MA 02111-1307|51 Franklin Street, Fifth Floor, Boston, MA 02110-1335|" src/opengl_spectrum.cpp

%build
%cmake .
%make_build

%install
%make_install

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;

%files
%license COPYING
%{_libdir}/kodi/addons/%{aname}/
%{_datadir}/kodi/addons/%{aname}/

%changelog
* Mon Apr 30 2018 Dominic Robinson <github@dcrdev.com> - 1.1.4-1
- Initial RPM Release