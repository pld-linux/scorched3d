Summary:	A 3D version of the classic DOS game Scorched Earth
Summary(pl):	Wersja 3D klasycznej DOS-owej gry Scorched Earth
Name:		scorched3d
Version:	36.1
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/Scorched3D-%{version}-src.tar.gz
# Source0-md5:	598f0e8da4c26f075a8b39185647e772
Source1:	%{name}.desktop
Patch0:		%{name}-types.patch
URL:		http://www.scorched3d.co.uk/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	wxGTK2-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Scorched 3D is a game based loosely on the classic DOS game Scorched
Earth "The Mother Of All Games".

%description -l pl
Scorched 3D jest gr± bazuj±c± na klasycznej DOS-owej grze Scorched
Earth.

%prep
%setup -q -n scorched
%patch0 -p1

%build
CXXFLAGS="-L/usr/X11R6/lib %{rpmcflags}"
%configure \
	--prefix=%{_datadir} \
	--with-wx-config=wxgtk2-2.4-config 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_datadir}

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

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
%{_desktopdir}/*
