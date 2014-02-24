%define beta beta7

%define __noautoprov '(.*)\\.so\\.0(.*)'
%define __noautoreq 'libgalan\\.so\\.(.*)'

Summary:	Graphical audio processing toolkit
Name:		galan
Version:	0.3.0
Release:	0.%{beta}.4
Source0:	%{name}-%{version}_%{beta}.tar.bz2
Url:		http://galan.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRequires:	fftw2-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(vorbis)

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

%files
%doc AUTHORS COPYING NEWS NOTES README TODO doc/examples doc/html
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}_%{beta}

%build
#autoreconf -fi
LDFLAGS="-lm -ldl" %configure2_5x --enable-static=no
make

%install
%makeinstall_std

#cleanup
for i in doc/CVS doc/examples/CVS doc/examples/samples/CVS doc/exdoc/html/CVS doc/html/CVS
do
rm -fr $i
done

rm -f %{buildroot}%{_libdir}/%{name}/libgalan.so

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Galan
Comment=Graphical audio processing toolkit
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;
EOF



