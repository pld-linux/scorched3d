Name:		scorched3d
Summary:	A 3D version of the classic DOS game Scorched Earth
Summary(pl):	Wersja 3D klasycznej DOS-owej gry Scorched Earth
Version:	36.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
URL:		http://www.scorched3d.co.uk
Source0:	http://dl.sourceforge.net/sourceforge/scorched3d/Scorched3D-%{version}-src.tar.gz
# Source0-md5:	598f0e8da4c26f075a8b39185647e772
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#BuildRequires:	perl, automake, autoconf, SDL-devel, wxGTK-devel
#BuildRequires:	SDL_mixer-devel, SDL_net-devel

%description
Scorched 3D is a game based loosely on the classic DOS game Scorched
Earth "The Mother Of All Games".

%prep
%setup -q -n scorched

%build
#sh ./autogen.sh
%configure \
	--prefix=%{_libdir} \
	CXXFLAGS="-L/usr/X11R6/lib %{rpmcflags}" \
	--with-wx-config=wxgtk2-2.4-config 

%{__make}

%install
rm -rf $R PM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/%{name}
%{_libdir}/%{name}}/data
