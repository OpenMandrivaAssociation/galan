%define major   0
%define libname %mklibname %name %major

Summary:    Graphical audio processing toolkit
Name:       galan
Version:    0.3.0
Release:    0.beta7.3

Source0:    %name-%{version}_beta7.tar.bz2
URL:        http://galan.sourceforge.net/
License:    GPLv2
Group:      Sound
BuildRoot:  %{_tmppath}/%{name}-buildroot
BuildRequires:  libalsa-devel libaudiofile-devel sndfile-devel
BuildRequires:  pkgconfig esound-devel libvorbis-devel
Buildrequires:  gtk2-devel gtkglarea-devel
BuildRequires:  fftw2-devel jackit-devel liblrdf-devel
Provides: libgalan0 = %version
Obsoletes: libgalan0

%description
Using gAlan is much like setting up an effects-chain for, say, a guitar.
You choose the effects units you wish to use, lay them out, and then
connect them to each other, starting with the guitar, threading through
the effects, and ending up at the amplifier (and ultimately the speakers).

It's not just limited to acting as an effects-chain, though. You can also
configure it (using the same basic principles) to act as a mixer, a
sample-sequencer or drum machine, or a synthesizer capable of emulating
various analogue systems. The examples page and the tutorial provide some
descriptions of some of the ways gAlan can be used. The User Guide has a
section on common motifs in mesh design which may also give an impression
of how gAlan works.

%prep
%setup -q -n %name-%{version}_beta7

%build
aclocal
autoconf
LDFLAGS="-lm -ldl" %configure --enable-static=no
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS NOTES README TODO doc/examples doc/html
%_bindir/*
%_libdir/%name
%_datadir/%name
%_datadir/applications/mandriva-%{name}.desktop


%changelog
* Fri Aug 31 2007 Funda Wang <fundawang@mandriva.org> 0.3.0-0.beta7.2mdv2008.0
+ Revision: 76656
- drop old menu & fix comment of menu entry

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Dec 08 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.0-0.beta7.1mdv2007.0
+ Revision: 93895
- New beta 7
  %%mkrel
  xdg menu
- Import galan

* Sat Sep 03 2005 Austin Acton <austin@mandriva.org> 0.3.0-0.beta5.1mdk
- beta5

* Sat Apr 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.0-0.beta3.3mdk
- fix conflict that prevent upgrading

* Tue Feb 17 2004 Austin Acton <austin@mandrake.org> 0.3.0-0.beta3.2mdk
- rebuild for liblrdf2

* Wed Feb 04 2004 Austin Acton <austin@mandrake.org> 0.3.0-0.beta3.1mdk
- 0.3.0beta3
- delib (useless)
- configure 2.5

