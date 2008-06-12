%define	name	galan
%define	version	0.3.0
%define	release	%mkrel 0.beta7.2

%define	major	0
%define	libname	%mklibname %name %major

Summary: 	Graphical audio processing toolkit
Name: 		%name
Version: 	%version
Release:	%release
Source0:	%name-%{version}_beta7.tar.bz2
URL: 		http://galan.sourceforge.net/
License: 	GPL
Group: 		Sound
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:  libalsa-devel libaudiofile-devel libsndfile-devel
BuildRequires:	pkgconfig esound-devel libvorbis-devel
Buildrequires:  gtk2-devel gtkglarea-devel
BuildRequires:	fftw2-devel jackit-devel liblrdf-devel
Provides: libgalan0 = %version
Obsoletes: libgalan0

%description
Using gAlan is much like setting up an effects-chain for, say, a guitar.
You choose the effects units you wish to use, lay them out, and then
connect them to each other, starting with the guitar, threading through
the effects, and ending up at the amplifier (and ultimately the speakers).

It's not just limited to acting as an effects-chain, though. You can also
configure it (using the same basic principles) to act as a mixer, a
sample-sequencer or drum machine, or a synthesiser capable of emulating
various analogue systems. The examples page and the tutorial provide some
descriptions of some of the ways gAlan can be used. The User Guide has a
section on common motifs in mesh design which may also give an impression
of how gAlan works.

%prep
%setup -q -n %name-%{version}_beta7

%build
%configure2_5x --enable-static=no
%make

%install
%makeinstall

#cleanup
for i in doc/CVS doc/examples/CVS doc/examples/samples/CVS doc/exdoc/html/CVS doc/html/CVS
do
rm -fr $i
done

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Galan
Comment=Graphical audio processing toolkit
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS NOTES README TODO doc/examples doc/html
%_bindir/*
%_libdir/%name
%_datadir/%name
%_datadir/applications/mandriva-%{name}.desktop
