Summary:	A 3D version of the classic DOS game Scorched Earth
Summary(pl.UTF-8):	Wersja 3D klasycznej DOS-owej gry Scorched Earth
Name:		scorched3d
Version:	43.3d
Release:	3
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/scorched3d/Scorched3D-%{version}-src.tar.gz
# Source0-md5:	9c3043282a9e7451468ff325bef3b04c
Source1:	%{name}.desktop
Patch0:		%{name}-types.patch
Patch1:		%{name}-openal.patch
Patch2:		%{name}-libpng15.patch
Patch3:		%{name}-gcc47.patch
URL:		http://www.scorched3d.co.uk/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	OpenAL-devel >= 0.0.8
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	fftw3-single-devel >= 3.0
BuildRequires:	freealut-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.533
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Scorched3D is a cross-platform 3D remake of the popular 2D artillery
game Scorched Earth. Scorched3D can be played against the computer,
other players, and remotely across the Internet or LAN.

%description -l pl.UTF-8
Scorched 3D to wieloplatformowe, trójwymiarowe odtworzenie popularnej
dwuwymiarowej gry artyleryjnej Scorched Earth. W Scorched3D można grać
przeciwko komputerowi, innym graczom oraz zdalnie poprzez Internet lub
LAN.

%prep
%setup -qc
mv scorched/* .
rm -rf scorched-dep-osx scorched
%undos src/common/porting/windows.h src/common/image/ImagePngFactory.cpp
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--datadir=%{_datadir}/%{name} \
	--with-wx-config=wx-gtk2-ansi-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=%{_datadir}/%{name}

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/documentation/*.txt

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
convert $RPM_BUILD_DIR/%{name}-%{version}/data/images/tank2.bmp $RPM_BUILD_ROOT%{_pixmapsdir}/scorched3d.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc documentation/*.txt
%attr(755,root,root) %{_bindir}/scorched3d
%attr(755,root,root) %{_bindir}/scorched3dc
%attr(755,root,root) %{_bindir}/scorched3ds
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/documentation
%{_pixmapsdir}/scorched3d.png
%{_desktopdir}/scorched3d.desktop
