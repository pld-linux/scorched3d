Name:		scorched3d
Summary:	A 3D version of the classic DOS game Scorched Earth
Summary(pl):	Wersja 3D klasycznej DOS-owej gry Scorched Earth
Version:	36.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
URL:		http://www.scorched3d.co.uk
Source0:	http://dl.sourceforge.net/sourceforge/scorched3d/Scorched3D-%{version}-src.tar.gz
# Source0-md5:	598f0e8da4c26f075a8b39185647e772
Source1:	scorched3d.desktop
BuildRequires:	wxGTK2-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires: ImageMagick-coder-png
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scorched 3D is a game based loosely on the classic DOS game Scorched
Earth "The Mother Of All Games".

%description -l pl
Scorched 3D jest gr± bazuj±c± na klasycznej DOSowej grze Scorched Earth.

%prep
%setup -q -n scorched

%build
%configure \
	CXXFLAGS="-L/usr/X11R6/lib %{rpmcflags}" \
	--prefix=%{_datadir} \
	--with-wx-config=wxgtk2-2.4-config 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_datadir}

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/documentation/*.txt

install -D %{SOURCE1} ${RPM_BUILD_ROOT}%{_desktopdir}/scorched3d.desktop
install -d ${RPM_BUILD_ROOT}%{_pixmapsdir}
convert $RPM_BUILD_DIR/scorched/data/windows/tank2.bmp $RPM_BUILD_ROOT%{_pixmapsdir}/scorched3d.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/%{name}
%doc documentation/*.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/documentation/
%{_pixmapsdir}/*
%{_desktopdir}/*
