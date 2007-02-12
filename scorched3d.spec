Summary:	A 3D version of the classic DOS game Scorched Earth
Summary(pl.UTF-8):   Wersja 3D klasycznej DOS-owej gry Scorched Earth
Name:		scorched3d
Version:	40.1b
%define		_ver	40.1b
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scorched3d/Scorched3D-%{_ver}-src.tar.gz
# Source0-md5:	bcf4a138149cc8070901e151027eb203
Source1:	%{name}.desktop
URL:		http://www.scorched3d.co.uk/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	OpenAL-devel >= 0.0.8
BuildRequires:	OpenGL-devel 
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	automake
BuildRequires:	freealut-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	wxGTK2-devel >= 2.6.0
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Scorched 3D is a game based loosely on the classic DOS game Scorched
Earth "The Mother Of All Games".

%description -l pl.UTF-8
Scorched 3D jest grą bazującą na klasycznej DOS-owej grze Scorched
Earth.

%prep
%setup -q -n scorched

%build
cp -f /usr/share/automake/config.sub .
CXXFLAGS="-L/usr/X11R6/%{_lib} %{rpmcflags}"
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
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/documentation
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
