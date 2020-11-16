%global aname visualization.spectrum
%global kodi_version 19.0
%global kodi_codename Matrix

Name:           kodi-visualization-spectrum
Version:        3.4.0
Release:        1%{?dist}
Summary:        Spectrum visualizer for Kodi
License:        GPLv2+
URL:            https://github.com/xbmc/visualization.spectrum
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{aname}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  pkgconfig(glm)
%ifarch %{arm} aarch64
BuildRequires:  libglvnd-devel
%else
BuildRequires:  pkgconfig(opengl)
%endif

Requires:       kodi >= %{kodi_version}

ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%setup -q -n %{aname}-%{version}-%{kodi_codename}

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.cpp' | xargs chmod a-x


%build
%cmake3
%cmake3_build


%install
%cmake3_install

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;


%files
%doc README.md
%license COPYING
%{_libdir}/kodi/addons/%{aname}/
%{_datadir}/kodi/addons/%{aname}/


%changelog
* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.0.3-1
- Bump to 2.0.3 (rfbz#5174)

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Dominic Robinson <github@dcrdev.com> - 2.0.2-1
- Bump to 2.0.2-1

* Mon Apr 30 2018 Dominic Robinson <github@dcrdev.com> - 1.1.4-1
- Initial RPM Release
