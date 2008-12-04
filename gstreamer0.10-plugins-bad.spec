%define version 0.10.9

%define release %mkrel 2
%define         _glib2          2.2
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
%define name %bname-plugins-bad
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%define build_experimental 1
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_amrwb 0
%define build_faac 0
%define build_faad 0
%define build_xvid 0
%define build_x264 0
%define build_dts 0
%define build_dirac 1
%define build_celt 0
%if %build_plf
%define distsuffix plf
%define build_amrwb 1
%define build_faac 1
%define build_faad 1
%define build_x264 1
%define build_xvid 1
%define build_dts 1
%endif

%define libname %mklibname gstapp0.10_ 0
%define libnamedev %mklibname -d gstapp0.10_ 0

Summary: 	GStreamer Streaming-media framework plug-ins
Name: 		%name
Version: 	%version
Release: 	%release
License: 	LGPLv2+ and GPLv2+
Group: 		Sound
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
Patch: gst-plugins-bad-0.10.7-wildmidi-timidity.cfg.patch
# gw: fix for bug #36437 (paths to realplayer codecs)
# prefer codecs from the RealPlayer package in restricted
Patch1: gst-plugins-bad-0.10.6-real-codecs-path.patch
Patch3: gst-plugins-bad-0.10.9-new-x264.patch
URL:            http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 
#gw for the pixbuf plugin
BuildRequires:  gtk+2-devel
BuildRequires:  glib2-devel >= %_glib2 
BuildRequires: libpng-devel >= 1.2.4-4mdk
BuildRequires: liboil-devel >= 0.3.2
BuildRequires: libSDL-devel
BuildRequires: libbzip2-devel
BuildRequires: libmodplug-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: exempi-devel
BuildRequires: openssl-devel
%ifarch %ix86
BuildRequires: nasm => 0.90
%endif
BuildRequires: valgrind libcheck-devel
BuildRequires: libgstreamer-plugins-base-devel >= %version
BuildRequires: libcdaudio-devel
BuildRequires: libsndfile-devel
Provides:	%bname-audiosrc
Provides:	%bname-audiosink
Obsoletes:	gstreamer0.10-fluendo-mpegdemux <= 0.10.15
Provides:	gstreamer0.10-fluendo-mpegdemux

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %build_plf
This package is in PLF as it violates some patents.
%endif


%package -n %bname-dc1394
Summary: GStreamer DC1394 plugin
Group: System/Libraries
BuildRequires: libdc1394-20-devel

%description -n %bname-dc1394
This is a IEEE 1394 (Firewire) support plugin for GStreamer.

%files -n %bname-dc1394
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstdc1394.so

%package -n %bname-ofa
Summary: GStreamer OFA plugin
Group: Sound
BuildRequires: libofa-devel
%description -n %bname-ofa
This is a metadata support plugin for GStreamer based on the Open
Fingerprint Architecture library.

%files -n %bname-ofa
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstofa.so

%package -n %bname-wildmidi
Summary: GStreamer wildmidi plugin
Group: Sound
BuildRequires: wildmidi-devel
Requires: timidity-instruments
%description -n %bname-wildmidi
This is a MIDI plugin for GStreamer based on the wildmidi library.

%files -n %bname-wildmidi
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstwildmidi.so

%package -n %bname-mpeg2enc
Summary:       GStreamer mjpegtools plug-in
Group:         Video
BuildRequires: libmjpegtools-devel

%description -n %bname-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %bname-mpeg2enc
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%_libdir/gstreamer-%majorminor/libgstmplex.so

%if %build_dirac
%package -n %bname-dirac
Summary:       GStreamer dirac plug-in
Group:         Video
BuildRequires: libdirac-devel >= 0.9

%description -n %bname-dirac
Dirac encoding and decoding plug-in.

%files -n %bname-dirac
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdirac.so
%endif

### LADSPA ###
%package -n %bname-ladspa
Summary: Gstreamer wrapper for LADSPA plug-ins
Group: Sound
Requires:      ladspa
BuildRequires: ladspa-devel

%description -n %bname-ladspa
Plug-in which wraps LADSPA plug-ins for use by GStreamer applications.
We suggest you also get the cmt package of ladspa plug-ins
and steve harris's swh-plugins package.

%files -n %bname-ladspa
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so

%package -n %bname-jack
Summary:  GStreamer plug-in for the Jack Sound Server
Group:    Sound
BuildRequires: libjack-devel => 0.28.0
Provides:	%bname-audiosrc
Provides:	%bname-audiosink

%description -n %bname-jack
Plug-in for the JACK professional sound server.

%files -n %bname-jack
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstjack.so

%if %build_dts
%package -n %bname-dts
Summary:GStreamer plug-ins for DTS audio playback
Group:         Sound
BuildRequires: dtsdec-devel

%description -n %bname-dts
Plug-ins for decoding DTS audio.

%files -n %bname-dts
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%endif

%if %build_xvid
%package -n %bname-xvid
Summary:GStreamer plug-ins for XVID video encoding and decoding
Group:         Video
BuildRequires: xvid-devel >= 1.1
 
%description -n %bname-xvid
Plug-ins for encoding and decoding XVID video.
 
This package is in PLF as it violates some patents.
%files -n %bname-xvid
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstxvid.so
%endif

%if %build_x264
%package -n %bname-x264
Summary:GStreamer plug-in for H264/AVC video encoding
Group:         Video
BuildRequires: libx264-devel
 
%description -n %bname-x264
Plug-in for encoding H264/AVC video.
 
This package is in PLF as it violates some patents.
%files -n %bname-x264
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstx264.so
%endif

%package -n %bname-musepack
Summary:GStreamer plug-in Musepack playback
Group:         Sound
BuildRequires: libmpcdec-devel
 
%description -n %bname-musepack
This plugin for GStreamer can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes mpc, mp+ or mpp.

%files -n %bname-musepack
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstmusepack.so

%package -n %bname-mms
Summary:       GStreamer plug-in for mms streams
Group:         System/Libraries
Requires:      %bname-plugins = %{version}
BuildRequires: libmms-devel

%description -n %bname-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %bname-mms
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so

%package -n %bname-directfb
Summary:       GStreamer plug-in for DirectFB output
Group: Video
Requires:      %bname-plugins = %{version}
BuildRequires: libdirectfb-devel

%description -n %bname-directfb
Plug-in supporting the video output to DirectFB.

%files -n %bname-directfb
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdfbvideosink.so

%package -n %bname-soundtouch
Summary:       GStreamer plug-in for SoundTouch support
Group: Sound
Requires:      %bname-plugins = %{version}
BuildRequires: libsoundtouch-devel

%description -n %bname-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %bname-soundtouch
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstsoundtouch.so

%package -n %bname-metadata
Summary:       GStreamer plug-in for metadata support
Group: System/Libraries
Requires:      %bname-plugins = %{version}
BuildRequires: libexif-devel
BuildRequires: libiptcdata-devel

%description -n %bname-metadata
Plug-in supporting several metadata formats.

%files -n %bname-metadata
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstmetadata.so

%if %build_experimental
%package -n %bname-resindvd
Summary: GStreamer DVD menu plugin
Group: Video
BuildRequires: libdvdnav-devel

%description -n %bname-resindvd
This is a DVD playback plugin for GStreamer with menu support.

%files -n %bname-resindvd
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libresindvd.so
%endif

%package -n %libname
Group: System/Libraries
Summary: GStreamer application library
%description -n %libname
This is the GStreamer application library.

%package -n %libnamedev
Group: Development/C
Summary: GStreamer application library
Requires: %libname = %version
%description -n %libnamedev
This is the GStreamer application library.


%package doc
Group: Books/Computer books
Summary: GStreamer application library
Requires: %libname = %version
%description doc
This is the documentation of %name.



%prep
%setup -q -n gst-plugins-bad-%{version}
%patch -p1
%patch1 -p1
%patch3 -p1
aclocal -I common/m4 -I m4
autoconf
automake

%build
%configure2_5x --disable-dependency-tracking \
%if %build_plf
  --with-package-name='PLF %name package' \
  --with-package-origin='http://plf.zarb.org/' \
%else
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \
%endif
%if ! %build_faac
	--disable-faac \
%endif
%if ! %build_faad
	--disable-faad \
%endif
%if ! %build_dirac
        --disable-dirac \
%endif
%if %build_experimental
	--enable-experimental
%endif

%make

%check
cd tests/check
make check

%install
rm -rf %buildroot gst-plugins-base-%majorminor.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang gst-plugins-bad-%majorminor
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files doc
%defattr(-, root, root)
%doc docs/plugins/html

%files -f gst-plugins-bad-%majorminor.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS 
%_libdir/gstreamer-%majorminor/libgstaiffparse.so
%_libdir/gstreamer-%majorminor/libgstapexsink.so
%_libdir/gstreamer-%majorminor/libgstapp.so
%_libdir/gstreamer-%majorminor/libgstbayer.so
%_libdir/gstreamer-%majorminor/libgstdccp.so
%_libdir/gstreamer-%majorminor/libgstdvb.so
%_libdir/gstreamer-%majorminor/libgstdvdspu.so
%_libdir/gstreamer-%majorminor/libgstfbdevsink.so
%_libdir/gstreamer-%majorminor/libgstflv.so
%_libdir/gstreamer-%majorminor/libgstfestival.so
%_libdir/gstreamer-%majorminor/libgstmpegdemux.so
%_libdir/gstreamer-%majorminor/libgstmpegtsmux.so
%_libdir/gstreamer-%majorminor/libgstmpegvideoparse.so
%_libdir/gstreamer-%majorminor/libgstmpeg4videoparse.so
%_libdir/gstreamer-%majorminor/libgstmve.so
%_libdir/gstreamer-%majorminor/libgstoss4audio.so
%_libdir/gstreamer-%majorminor/libgstpcapparse.so
%_libdir/gstreamer-%majorminor/libgstscaletempoplugin.so
%_libdir/gstreamer-%majorminor/libgstrawparse.so
%_libdir/gstreamer-%majorminor/libgstreal.so
%_libdir/gstreamer-%majorminor/libgstrtpmanager.so
%_libdir/gstreamer-%majorminor/libgstsdpelem.so
%_libdir/gstreamer-%majorminor/libgstselector.so
%_libdir/gstreamer-%majorminor/libgstsndfile.so
%_libdir/gstreamer-%majorminor/libgstspeexresample.so
%_libdir/gstreamer-%majorminor/libgststereo.so
%_libdir/gstreamer-%majorminor/libgstsubenc.so
%_libdir/gstreamer-%majorminor/libgstvcdsrc.so
%_libdir/gstreamer-%majorminor/libgstvideosignal.so
%_libdir/gstreamer-%majorminor/libgstvmnc.so
%_libdir/gstreamer-%majorminor/libgstalsaspdif.so
%_libdir/gstreamer-%majorminor/libgstbz2.so
%_libdir/gstreamer-%majorminor/libgstcdaudio.so
%_libdir/gstreamer-%majorminor/libgstcdxaparse.so
%_libdir/gstreamer-%majorminor/libgstdeinterlace.so
%if %build_experimental
%_libdir/gstreamer-%majorminor/libgstdeinterlace2.so
%endif
%_libdir/gstreamer-%majorminor/libgstfilter.so
%_libdir/gstreamer-%majorminor/libgstfreeze.so
%_libdir/gstreamer-%majorminor/libgsth264parse.so
%_libdir/gstreamer-%majorminor/libgstmodplug.so
%_libdir/gstreamer-%majorminor/libgstnsf.so
%_libdir/gstreamer-%majorminor/libgstnuvdemux.so
%_libdir/gstreamer-%majorminor/libgstrfbsrc.so
%_libdir/gstreamer-%majorminor/libgstsdl.so
%_libdir/gstreamer-%majorminor/libgstspeed.so
%_libdir/gstreamer-%majorminor/libgsttrm.so
%_libdir/gstreamer-%majorminor/libgsttta.so
%_libdir/gstreamer-%majorminor/libgsty4menc.so

%if %build_faad
%package -n %bname-faad
Summary:GStreamer plug-ins for AAC audio playback
Group:         Sound
Requires: %bname-plugins >= %version
BuildRequires: libfaad2-devel => 2.0
 
%description -n %bname-faad
Plug-ins for playing AAC audio
 
This package is in PLF as it violates some patents.
%files -n %bname-faad
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstfaad.so
%endif

%if %build_faac
%package -n %bname-faac
Summary:GStreamer plug-ins for AAC audio encoding
Group:         Sound
Requires: %bname-plugins >= %version
BuildRequires: libfaac-devel
 
%description -n %bname-faac
Plug-ins for encoding AAC audio
 
This package is in PLF as it violates some patents.
%files -n %bname-faac
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstfaac.so
%endif

%package -n %bname-gsm
Summary: GStreamer plugin for GSM lossy audio format
Group: Sound
Requires: %bname-plugins >= %{version}
BuildRequires: gsm-devel >= 1.0.10

%description -n %bname-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%files -n %bname-gsm
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so

%if 0
### SWFDEC FLASH PLUGIN ###
%package -n %bname-swfdec
Summary:  GStreamer Flash rendering plug-in
Group:    System/Libraries
Requires: %bname-plugins = %{version}
BuildRequires: libswfdec-devel => 0.3.0

%description -n %bname-swfdec
Plug-in for rendering Flash animations using swfdec library

%files -n %bname-swfdec
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so
%endif

%package -n %bname-neon
Summary:  GStreamer HTTP plugin based on libneon
Group:    System/Libraries
Requires: %bname-plugins = %{version}
BuildRequires: neon0.27-devel

%description -n %bname-neon
Plug-in for HTTP access based on libneon.

%files -n %bname-neon
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so

%package -n %bname-nas
Summary:  Gstreamer output plugin for the NAS sound server
Group:    Sound
Requires: %bname-plugins = %{version}
BuildRequires: libnas-devel

%description -n %bname-nas
Output plugin for GStreamer for use with the nas sound server.

%files -n %bname-nas
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstnassink.so

%files -n %libname
%defattr(-, root, root)
%_libdir/libgstapp-0.10.so.0*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/libgstapp-0.10.so
%_includedir/gstreamer-0.10/gst/app/

%if %build_amrwb
%package -n %bname-amrwb
Summary: GStreamer plug-in for AMR-WB support
Group:  Sound
Requires: %bname-plugins >= %{version}
BuildRequires: libamrwb-devel

%description -n %bname-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in PLF as it violates some patents.
%files -n %bname-amrwb
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstamrwb.so
%endif

%package -n %bname-twolame
Summary: GStreamer plug-in for MP2 encoding support
Group:  Sound
Requires: %bname-plugins >= %{version}
BuildRequires: libtwolame-devel

%description -n %bname-twolame
Plug-in for encoding MP2 under GStreamer.

%files -n %bname-twolame
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgsttwolame.so

%package -n %bname-jp2k
Summary: GStreamer plug-in for JPEG2000 support
Group:  Graphics
Requires: %bname-plugins >= %{version}
BuildRequires: libjasper-devel

%description -n %bname-jp2k
Plug-in for JPEG2000 support under GStreamer.

%files -n %bname-jp2k
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstjp2k.so

%if %build_celt
%package -n %bname-celt
Summary: GStreamer plug-in for CELT support
Group:  Video
Requires: %bname-plugins >= %{version}
#gw 0.10.9 doesn't build with 0.5.0
BuildRequires: celt-devel < 0.5.0

%description -n %bname-celt
Plug-in for CELT support under GStreamer.

%files -n %bname-celt
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstcelt.so
%endif
