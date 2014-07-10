Summary:	Open-source X.org video driver for NVIDIA Tegra processors
Summary(pl.UTF-8):	Mający otwarte źródła sterownik obrazu X.org dla procesorów NVIDIA Tegra
Name:		xorg-driver-video-opentegra
Version:	0.7.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-video-opentegra-%{version}.tar.xz
# Source0-md5:	dc7f48452d7df4bd0330c6576ba885c2
URL:		http://opentegra.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.2
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel
# >= 1.16 for output class config
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.2
Requires:	xorg-xserver-server
Provides:	xorg-driver-video
ExclusiveArch:	arm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open-source X.org video driver for NVIDIA Tegra processors. It
supports all NVIDIA Tegra hardware that is supported by the Linux
kernel DRM driver.

%description -l pl.UTF-8
Mający otwarte źródła sterownik obrazu X.org dla procesorów NVIDIA
Tegra. Obsługuje wszystkie układy NVIDIA Tegra, obsługiwane przez
sterownik DRM jądra Linuksa.

%prep
%setup -q -n xf86-video-opentegra-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/opentegra_drv.so
%{_mandir}/man4/opentegra.4*
