Summary:	A 3D version of the classic DOS game Scorched Earth
Summary(pl.UTF-8):	Wersja 3D klasycznej DOS-owej gry Scorched Earth
Name:		scorched3d
Version:	41.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scorched3d/Scorched3D-%{version}-src.tar.gz
# Source0-md5:	6bb47045abccaca1f775ff4cde8b3b5d
Source1:	%{name}.desktop
Patch0:		%{name}-types.patch
URL:		http://www.scorched3d.co.uk/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	OpenAL-devel >= 0.0.8
BuildRequires:	OpenGL-GLU-devel 
BuildRequires:	SDL_net-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	automake
BuildRequires:	fftw3-single-devel >= 3.0
BuildRequires:	freealut-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
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
%setup -q -n scorched
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
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

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/documentation/*.txt

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
convert $RPM_BUILD_DIR/scorched/data/windows/tank2.bmp $RPM_BUILD_ROOT%{_pixmapsdir}/scorched3d.png

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
