# Makefile.in generated by automake 1.11.3 from Makefile.am.
# src/Makefile.  Generated from Makefile.in by configure.

# Copyright (C) 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
# 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011 Free Software
# Foundation, Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.





pkgdatadir = $(datadir)/dvdauthor
pkgincludedir = $(includedir)/dvdauthor
pkglibdir = $(libdir)/dvdauthor
pkglibexecdir = $(libexecdir)/dvdauthor
am__cd = CDPATH="$${ZSH_VERSION+.}$(PATH_SEPARATOR)" && cd
install_sh_DATA = $(install_sh) -c -m 644
install_sh_PROGRAM = $(install_sh) -c
install_sh_SCRIPT = $(install_sh) -c
INSTALL_HEADER = $(INSTALL_DATA)
transform = $(program_transform_name)
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
build_triplet = x86_64-unknown-linux-gnu
host_triplet = x86_64-unknown-linux-gnu
bin_PROGRAMS = dvdauthor$(EXEEXT) spumux$(EXEEXT) spuunmux$(EXEEXT) \
	mpeg2desc$(EXEEXT) $(am__EXEEXT_1)
am__append_1 = dvdunauthor
subdir = src
DIST_COMMON = $(srcdir)/Makefile.am $(srcdir)/Makefile.in \
	$(srcdir)/config.h.in
ACLOCAL_M4 = $(top_srcdir)/aclocal.m4
am__aclocal_m4_deps = $(top_srcdir)/configure.ac
am__configure_deps = $(am__aclocal_m4_deps) $(CONFIGURE_DEPENDENCIES) \
	$(ACLOCAL_M4)
mkinstalldirs = $(install_sh) -d
CONFIG_HEADER = config.h
CONFIG_CLEAN_FILES =
CONFIG_CLEAN_VPATH_FILES =
am__EXEEXT_1 = dvdunauthor$(EXEEXT)
am__installdirs = "$(DESTDIR)$(bindir)" "$(DESTDIR)$(bindir)"
PROGRAMS = $(bin_PROGRAMS)
am_dvdauthor_OBJECTS = dvdauthor.$(OBJEXT) dvdcompile.$(OBJEXT) \
	dvdvml.$(OBJEXT) dvdvmy.$(OBJEXT) dvdifo.$(OBJEXT) \
	dvdvob.$(OBJEXT) dvdpgc.$(OBJEXT) dvdcli.$(OBJEXT) \
	readxml.$(OBJEXT) conffile.$(OBJEXT) compat.$(OBJEXT)
dvdauthor_OBJECTS = $(am_dvdauthor_OBJECTS)
am__DEPENDENCIES_1 =
dvdauthor_DEPENDENCIES = $(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1)
am_dvdunauthor_OBJECTS = dvdunauthor.$(OBJEXT) dvduncompile.$(OBJEXT) \
	compat.$(OBJEXT)
dvdunauthor_OBJECTS = $(am_dvdunauthor_OBJECTS)
dvdunauthor_DEPENDENCIES = $(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1)
am_mpeg2desc_OBJECTS = mpeg2desc.$(OBJEXT) compat.$(OBJEXT)
mpeg2desc_OBJECTS = $(am_mpeg2desc_OBJECTS)
mpeg2desc_DEPENDENCIES = $(am__DEPENDENCIES_1)
am_spumux_OBJECTS = subgen.$(OBJEXT) subgen-parse-xml.$(OBJEXT) \
	readxml.$(OBJEXT) subgen-encode.$(OBJEXT) \
	subgen-image.$(OBJEXT) conffile.$(OBJEXT) compat.$(OBJEXT) \
	subrender.$(OBJEXT) subreader.$(OBJEXT) subfont.$(OBJEXT)
spumux_OBJECTS = $(am_spumux_OBJECTS)
spumux_DEPENDENCIES = $(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1) \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1) \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1)
am_spuunmux_OBJECTS = spuunmux-spuunmux.$(OBJEXT) \
	spuunmux-compat.$(OBJEXT) spuunmux-conffile.$(OBJEXT)
spuunmux_OBJECTS = $(am_spuunmux_OBJECTS)
spuunmux_DEPENDENCIES = $(am__DEPENDENCIES_1)
spuunmux_LINK = $(CCLD) $(spuunmux_CFLAGS) $(CFLAGS) $(AM_LDFLAGS) \
	$(LDFLAGS) -o $@
am__vpath_adj_setup = srcdirstrip=`echo "$(srcdir)" | sed 's|.|.|g'`;
am__vpath_adj = case $$p in \
    $(srcdir)/*) f=`echo "$$p" | sed "s|^$$srcdirstrip/||"`;; \
    *) f=$$p;; \
  esac;
am__strip_dir = f=`echo $$p | sed -e 's|^.*/||'`;
am__install_max = 40
am__nobase_strip_setup = \
  srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*|]/\\\\&/g'`
am__nobase_strip = \
  for p in $$list; do echo "$$p"; done | sed -e "s|$$srcdirstrip/||"
am__nobase_list = $(am__nobase_strip_setup); \
  for p in $$list; do echo "$$p $$p"; done | \
  sed "s| $$srcdirstrip/| |;"' / .*\//!s/ .*/ ./; s,\( .*\)/[^/]*$$,\1,' | \
  $(AWK) 'BEGIN { files["."] = "" } { files[$$2] = files[$$2] " " $$1; \
    if (++n[$$2] == $(am__install_max)) \
      { print $$2, files[$$2]; n[$$2] = 0; files[$$2] = "" } } \
    END { for (dir in files) print dir, files[dir] }'
am__base_list = \
  sed '$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;s/\n/ /g' | \
  sed '$$!N;$$!N;$$!N;$$!N;s/\n/ /g'
am__uninstall_files_from_dir = { \
  test -z "$$files" \
    || { test ! -d "$$dir" && test ! -f "$$dir" && test ! -r "$$dir"; } \
    || { echo " ( cd '$$dir' && rm -f" $$files ")"; \
         $(am__cd) "$$dir" && rm -f $$files; }; \
  }
SCRIPTS = $(nodist_bin_SCRIPTS)
DEFAULT_INCLUDES = -I.
depcomp = $(SHELL) $(top_srcdir)/autotools/depcomp
am__depfiles_maybe = depfiles
am__mv = mv -f
COMPILE = $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) \
	$(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)
CCLD = $(CC)
LINK = $(CCLD) $(AM_CFLAGS) $(CFLAGS) $(AM_LDFLAGS) $(LDFLAGS) -o $@
SOURCES = $(dvdauthor_SOURCES) $(dvdunauthor_SOURCES) \
	$(mpeg2desc_SOURCES) $(spumux_SOURCES) $(spuunmux_SOURCES)
DIST_SOURCES = $(dvdauthor_SOURCES) $(dvdunauthor_SOURCES) \
	$(mpeg2desc_SOURCES) $(spumux_SOURCES) $(spuunmux_SOURCES)
ETAGS = etags
CTAGS = ctags
DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)
ACLOCAL = ${SHELL} /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/autotools/missing --run aclocal-1.11
AMTAR = $${TAR-tar}
AUTOCONF = ${SHELL} /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/autotools/missing --run autoconf
AUTOHEADER = ${SHELL} /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/autotools/missing --run autoheader
AUTOMAKE = ${SHELL} /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/autotools/missing --run automake-1.11
AWK = gawk
CC = gcc
CCDEPMODE = depmode=gcc3
CFLAGS = -g -O2
CPP = gcc -E
CPPFLAGS = 
CYGPATH_W = echo
DEFS = -DHAVE_CONFIG_H
DEPDIR = .deps
ECHO_C = 
ECHO_N = -n
ECHO_T = 
EGREP = /bin/grep -E
EXEEXT = 
FONTCONFIG_CFLAGS = 
FONTCONFIG_LIBS = 
FREETYPECONFIG = freetype-config
FREETYPE_CPPFLAGS = -I/usr/include/freetype2
FREETYPE_LIBS = -L/usr/lib/x86_64-linux-gnu -lfreetype -lz
FRIBIDI_CFLAGS = 
FRIBIDI_LIBS = 
GMAGICKCONFIG = 
GREP = /bin/grep
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL_STRIP_PROGRAM = $(install_sh) -c -s
LDFLAGS = 
LIBICONV = 
LIBOBJS = 
LIBPNG_CFLAGS = -I/usr/include/libpng12  
LIBPNG_LIBS = -lpng12  
LIBS = 
LTLIBICONV = 
LTLIBOBJS = 
MAGICKCONFIG = 
MAGICK_CPPFLAGS = -I/usr/include/libpng12  
MAGICK_LIBS = -lpng12  
MAKEINFO = ${SHELL} /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/autotools/missing --run makeinfo
MKDIR_P = /bin/mkdir -p
OBJEXT = o
PACKAGE = dvdauthor
PACKAGE_BUGREPORT = dvdauthor-users@lists.sourceforge.net
PACKAGE_NAME = DVDAuthor
PACKAGE_STRING = DVDAuthor 0.7.1+
PACKAGE_TARNAME = dvdauthor
PACKAGE_URL = 
PACKAGE_VERSION = 0.7.1+
PATH_SEPARATOR = :
PKG_CONFIG = /usr/bin/pkg-config
PKG_CONFIG_LIBDIR = 
PKG_CONFIG_PATH = 
SET_MAKE = 
SHELL = /bin/bash
STRIP = 
VERSION = 0.7.1+
XML2_CONFIG = /usr/bin/xml2-config
XML_CPPFLAGS = -I/usr/include/libxml2
XML_LIBS = -L/usr/lib/x86_64-linux-gnu -lxml2
abs_builddir = /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/src
abs_srcdir = /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/src
abs_top_builddir = /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor
abs_top_srcdir = /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor
ac_ct_CC = gcc
am__include = include
am__leading_dot = .
am__quote = 
am__tar = $${TAR-tar} chof - "$$tardir"
am__untar = $${TAR-tar} xf -
bindir = ${exec_prefix}/bin
build = x86_64-unknown-linux-gnu
build_alias = 
build_cpu = x86_64
build_os = linux-gnu
build_vendor = unknown
builddir = .
datadir = ${datarootdir}
datarootdir = ${prefix}/share
docdir = ${datarootdir}/doc/${PACKAGE_TARNAME}
dvidir = ${docdir}
exec_prefix = ${prefix}
host = x86_64-unknown-linux-gnu
host_alias = 
host_cpu = x86_64
host_os = linux-gnu
host_vendor = unknown
htmldir = ${docdir}
includedir = ${prefix}/include
infodir = ${datarootdir}/info
install_sh = ${SHELL} /home/aoanla/Documents/Projects/derby-dvd-tool/dvdauthor/autotools/install-sh
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/libexec
localedir = ${datarootdir}/locale
localstatedir = ${prefix}/var
mandir = ${datarootdir}/man
mkdir_p = /bin/mkdir -p
oldincludedir = /usr/include
pdfdir = ${docdir}
prefix = /usr/local
program_transform_name = s,x,x,
psdir = ${docdir}
sbindir = ${exec_prefix}/sbin
sharedstatedir = ${prefix}/com
srcdir = .
sysconfdir = ${prefix}/etc
target_alias = 
top_build_prefix = ../
top_builddir = ..
top_srcdir = ..
nodist_bin_SCRIPTS = dvddirdel
AM_CPPFLAGS = -DSYSCONFDIR="\"$(sysconfdir)\"" \
    -I/usr/include/libxml2 -I/usr/include/libpng12   -I/usr/include/freetype2  

AM_CFLAGS = -Wall
dvdauthor_SOURCES = dvdauthor.c common.h dvdauthor.h da-internal.h \
    dvdcompile.c dvdvm.h dvdvml.c dvdvmy.c dvdvmy.h \
    dvdifo.c dvdvob.c dvdpgc.c \
    dvdcli.c readxml.c readxml.h \
    conffile.c conffile.h compat.c compat.h rgb.h

dvdauthor_LDADD = $(LIBICONV) $(XML_LIBS)
dvdunauthor_SOURCES = dvdunauthor.c dvduncompile.c common.h dvduncompile.h compat.c compat.h
dvdunauthor_LDADD = $(XML_LIBS) $(LIBICONV) -ldvdread
spumux_SOURCES = subgen.c subgen.h rgb.h \
    subgen-parse-xml.c readxml.c readxml.h \
    subgen-encode.c subgen-image.c subglobals.h \
    conffile.c conffile.h compat.c compat.h common.h \
    subrender.c subrender.h subreader.c subreader.h subfont.c subfont.h

spumux_LDADD = $(XML_LIBS) $(MAGICK_LIBS) $(FREETYPE_LIBS) \
    $(FRIBIDI_LIBS) $(FONTCONFIG_LIBS) $(LIBICONV) -lm

spuunmux_SOURCES = spuunmux.c rgb.h compat.c compat.h common.h conffile.h conffile.c
spuunmux_CFLAGS = -I/usr/include/libpng12   $(AM_CFLAGS)
spuunmux_LDADD = $(LIBICONV) -lpng12  
mpeg2desc_SOURCES = common.h mpeg2desc.c compat.c
mpeg2desc_LDADD = $(LIBICONV)
edit = sed \
    -e 's,@sysconfdir\@,$(sysconfdir),g' \
    -e 's,@PACKAGE_NAME\@,DVDAuthor,g' \
    -e 's,@PACKAGE_VERSION\@,0.7.1+,g' \
    -e 's,@PACKAGE_BUGREPORT\@,dvdauthor-users@lists.sourceforge.net,g'

EXTRA_DIST = dvdvml.l dvdvmy.y dvddirdel.in
MOSTLYCLEANFILES = dvddirdel
MAINTAINERCLEANFILES = dvdvml.c dvdvmy.c dvdvmy.h
FLEX = flex
BISON = bison
all: config.h
	$(MAKE) $(AM_MAKEFLAGS) all-am

.SUFFIXES:
.SUFFIXES: .c .o .obj
$(srcdir)/Makefile.in:  $(srcdir)/Makefile.am  $(am__configure_deps)
	@for dep in $?; do \
	  case '$(am__configure_deps)' in \
	    *$$dep*) \
	      ( cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh ) \
	        && { if test -f $@; then exit 0; else break; fi; }; \
	      exit 1;; \
	  esac; \
	done; \
	echo ' cd $(top_srcdir) && $(AUTOMAKE) --gnu src/Makefile'; \
	$(am__cd) $(top_srcdir) && \
	  $(AUTOMAKE) --gnu src/Makefile
.PRECIOUS: Makefile
Makefile: $(srcdir)/Makefile.in $(top_builddir)/config.status
	@case '$?' in \
	  *config.status*) \
	    cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh;; \
	  *) \
	    echo ' cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe)'; \
	    cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe);; \
	esac;

$(top_builddir)/config.status: $(top_srcdir)/configure $(CONFIG_STATUS_DEPENDENCIES)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh

$(top_srcdir)/configure:  $(am__configure_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(ACLOCAL_M4):  $(am__aclocal_m4_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(am__aclocal_m4_deps):

config.h: stamp-h1
	@if test ! -f $@; then rm -f stamp-h1; else :; fi
	@if test ! -f $@; then $(MAKE) $(AM_MAKEFLAGS) stamp-h1; else :; fi

stamp-h1: $(srcdir)/config.h.in $(top_builddir)/config.status
	@rm -f stamp-h1
	cd $(top_builddir) && $(SHELL) ./config.status src/config.h
$(srcdir)/config.h.in:  $(am__configure_deps) 
	($(am__cd) $(top_srcdir) && $(AUTOHEADER))
	rm -f stamp-h1
	touch $@

distclean-hdr:
	-rm -f config.h stamp-h1
install-binPROGRAMS: $(bin_PROGRAMS)
	@$(NORMAL_INSTALL)
	test -z "$(bindir)" || $(MKDIR_P) "$(DESTDIR)$(bindir)"
	@list='$(bin_PROGRAMS)'; test -n "$(bindir)" || list=; \
	for p in $$list; do echo "$$p $$p"; done | \
	sed 's/$(EXEEXT)$$//' | \
	while read p p1; do if test -f $$p; \
	  then echo "$$p"; echo "$$p"; else :; fi; \
	done | \
	sed -e 'p;s,.*/,,;n;h' -e 's|.*|.|' \
	    -e 'p;x;s,.*/,,;s/$(EXEEXT)$$//;$(transform);s/$$/$(EXEEXT)/' | \
	sed 'N;N;N;s,\n, ,g' | \
	$(AWK) 'BEGIN { files["."] = ""; dirs["."] = 1 } \
	  { d=$$3; if (dirs[d] != 1) { print "d", d; dirs[d] = 1 } \
	    if ($$2 == $$4) files[d] = files[d] " " $$1; \
	    else { print "f", $$3 "/" $$4, $$1; } } \
	  END { for (d in files) print "f", d, files[d] }' | \
	while read type dir files; do \
	    if test "$$dir" = .; then dir=; else dir=/$$dir; fi; \
	    test -z "$$files" || { \
	      echo " $(INSTALL_PROGRAM_ENV) $(INSTALL_PROGRAM) $$files '$(DESTDIR)$(bindir)$$dir'"; \
	      $(INSTALL_PROGRAM_ENV) $(INSTALL_PROGRAM) $$files "$(DESTDIR)$(bindir)$$dir" || exit $$?; \
	    } \
	; done

uninstall-binPROGRAMS:
	@$(NORMAL_UNINSTALL)
	@list='$(bin_PROGRAMS)'; test -n "$(bindir)" || list=; \
	files=`for p in $$list; do echo "$$p"; done | \
	  sed -e 'h;s,^.*/,,;s/$(EXEEXT)$$//;$(transform)' \
	      -e 's/$$/$(EXEEXT)/' `; \
	test -n "$$list" || exit 0; \
	echo " ( cd '$(DESTDIR)$(bindir)' && rm -f" $$files ")"; \
	cd "$(DESTDIR)$(bindir)" && rm -f $$files

clean-binPROGRAMS:
	-test -z "$(bin_PROGRAMS)" || rm -f $(bin_PROGRAMS)
dvdauthor$(EXEEXT): $(dvdauthor_OBJECTS) $(dvdauthor_DEPENDENCIES) $(EXTRA_dvdauthor_DEPENDENCIES) 
	@rm -f dvdauthor$(EXEEXT)
	$(LINK) $(dvdauthor_OBJECTS) $(dvdauthor_LDADD) $(LIBS)
dvdunauthor$(EXEEXT): $(dvdunauthor_OBJECTS) $(dvdunauthor_DEPENDENCIES) $(EXTRA_dvdunauthor_DEPENDENCIES) 
	@rm -f dvdunauthor$(EXEEXT)
	$(LINK) $(dvdunauthor_OBJECTS) $(dvdunauthor_LDADD) $(LIBS)
mpeg2desc$(EXEEXT): $(mpeg2desc_OBJECTS) $(mpeg2desc_DEPENDENCIES) $(EXTRA_mpeg2desc_DEPENDENCIES) 
	@rm -f mpeg2desc$(EXEEXT)
	$(LINK) $(mpeg2desc_OBJECTS) $(mpeg2desc_LDADD) $(LIBS)
spumux$(EXEEXT): $(spumux_OBJECTS) $(spumux_DEPENDENCIES) $(EXTRA_spumux_DEPENDENCIES) 
	@rm -f spumux$(EXEEXT)
	$(LINK) $(spumux_OBJECTS) $(spumux_LDADD) $(LIBS)
spuunmux$(EXEEXT): $(spuunmux_OBJECTS) $(spuunmux_DEPENDENCIES) $(EXTRA_spuunmux_DEPENDENCIES) 
	@rm -f spuunmux$(EXEEXT)
	$(spuunmux_LINK) $(spuunmux_OBJECTS) $(spuunmux_LDADD) $(LIBS)
install-nodist_binSCRIPTS: $(nodist_bin_SCRIPTS)
	@$(NORMAL_INSTALL)
	test -z "$(bindir)" || $(MKDIR_P) "$(DESTDIR)$(bindir)"
	@list='$(nodist_bin_SCRIPTS)'; test -n "$(bindir)" || list=; \
	for p in $$list; do \
	  if test -f "$$p"; then d=; else d="$(srcdir)/"; fi; \
	  if test -f "$$d$$p"; then echo "$$d$$p"; echo "$$p"; else :; fi; \
	done | \
	sed -e 'p;s,.*/,,;n' \
	    -e 'h;s|.*|.|' \
	    -e 'p;x;s,.*/,,;$(transform)' | sed 'N;N;N;s,\n, ,g' | \
	$(AWK) 'BEGIN { files["."] = ""; dirs["."] = 1; } \
	  { d=$$3; if (dirs[d] != 1) { print "d", d; dirs[d] = 1 } \
	    if ($$2 == $$4) { files[d] = files[d] " " $$1; \
	      if (++n[d] == $(am__install_max)) { \
		print "f", d, files[d]; n[d] = 0; files[d] = "" } } \
	    else { print "f", d "/" $$4, $$1 } } \
	  END { for (d in files) print "f", d, files[d] }' | \
	while read type dir files; do \
	     if test "$$dir" = .; then dir=; else dir=/$$dir; fi; \
	     test -z "$$files" || { \
	       echo " $(INSTALL_SCRIPT) $$files '$(DESTDIR)$(bindir)$$dir'"; \
	       $(INSTALL_SCRIPT) $$files "$(DESTDIR)$(bindir)$$dir" || exit $$?; \
	     } \
	; done

uninstall-nodist_binSCRIPTS:
	@$(NORMAL_UNINSTALL)
	@list='$(nodist_bin_SCRIPTS)'; test -n "$(bindir)" || exit 0; \
	files=`for p in $$list; do echo "$$p"; done | \
	       sed -e 's,.*/,,;$(transform)'`; \
	dir='$(DESTDIR)$(bindir)'; $(am__uninstall_files_from_dir)

mostlyclean-compile:
	-rm -f *.$(OBJEXT)

distclean-compile:
	-rm -f *.tab.c

include ./$(DEPDIR)/compat.Po
include ./$(DEPDIR)/conffile.Po
include ./$(DEPDIR)/dvdauthor.Po
include ./$(DEPDIR)/dvdcli.Po
include ./$(DEPDIR)/dvdcompile.Po
include ./$(DEPDIR)/dvdifo.Po
include ./$(DEPDIR)/dvdpgc.Po
include ./$(DEPDIR)/dvdunauthor.Po
include ./$(DEPDIR)/dvduncompile.Po
include ./$(DEPDIR)/dvdvml.Po
include ./$(DEPDIR)/dvdvmy.Po
include ./$(DEPDIR)/dvdvob.Po
include ./$(DEPDIR)/mpeg2desc.Po
include ./$(DEPDIR)/readxml.Po
include ./$(DEPDIR)/spuunmux-compat.Po
include ./$(DEPDIR)/spuunmux-conffile.Po
include ./$(DEPDIR)/spuunmux-spuunmux.Po
include ./$(DEPDIR)/subfont.Po
include ./$(DEPDIR)/subgen-encode.Po
include ./$(DEPDIR)/subgen-image.Po
include ./$(DEPDIR)/subgen-parse-xml.Po
include ./$(DEPDIR)/subgen.Po
include ./$(DEPDIR)/subreader.Po
include ./$(DEPDIR)/subrender.Po

.c.o:
	$(COMPILE) -MT $@ -MD -MP -MF $(DEPDIR)/$*.Tpo -c -o $@ $<
	$(am__mv) $(DEPDIR)/$*.Tpo $(DEPDIR)/$*.Po
#	source='$<' object='$@' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(COMPILE) -c $<

.c.obj:
	$(COMPILE) -MT $@ -MD -MP -MF $(DEPDIR)/$*.Tpo -c -o $@ `$(CYGPATH_W) '$<'`
	$(am__mv) $(DEPDIR)/$*.Tpo $(DEPDIR)/$*.Po
#	source='$<' object='$@' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(COMPILE) -c `$(CYGPATH_W) '$<'`

spuunmux-spuunmux.o: spuunmux.c
	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -MT spuunmux-spuunmux.o -MD -MP -MF $(DEPDIR)/spuunmux-spuunmux.Tpo -c -o spuunmux-spuunmux.o `test -f 'spuunmux.c' || echo '$(srcdir)/'`spuunmux.c
	$(am__mv) $(DEPDIR)/spuunmux-spuunmux.Tpo $(DEPDIR)/spuunmux-spuunmux.Po
#	source='spuunmux.c' object='spuunmux-spuunmux.o' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -c -o spuunmux-spuunmux.o `test -f 'spuunmux.c' || echo '$(srcdir)/'`spuunmux.c

spuunmux-spuunmux.obj: spuunmux.c
	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -MT spuunmux-spuunmux.obj -MD -MP -MF $(DEPDIR)/spuunmux-spuunmux.Tpo -c -o spuunmux-spuunmux.obj `if test -f 'spuunmux.c'; then $(CYGPATH_W) 'spuunmux.c'; else $(CYGPATH_W) '$(srcdir)/spuunmux.c'; fi`
	$(am__mv) $(DEPDIR)/spuunmux-spuunmux.Tpo $(DEPDIR)/spuunmux-spuunmux.Po
#	source='spuunmux.c' object='spuunmux-spuunmux.obj' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -c -o spuunmux-spuunmux.obj `if test -f 'spuunmux.c'; then $(CYGPATH_W) 'spuunmux.c'; else $(CYGPATH_W) '$(srcdir)/spuunmux.c'; fi`

spuunmux-compat.o: compat.c
	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -MT spuunmux-compat.o -MD -MP -MF $(DEPDIR)/spuunmux-compat.Tpo -c -o spuunmux-compat.o `test -f 'compat.c' || echo '$(srcdir)/'`compat.c
	$(am__mv) $(DEPDIR)/spuunmux-compat.Tpo $(DEPDIR)/spuunmux-compat.Po
#	source='compat.c' object='spuunmux-compat.o' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -c -o spuunmux-compat.o `test -f 'compat.c' || echo '$(srcdir)/'`compat.c

spuunmux-compat.obj: compat.c
	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -MT spuunmux-compat.obj -MD -MP -MF $(DEPDIR)/spuunmux-compat.Tpo -c -o spuunmux-compat.obj `if test -f 'compat.c'; then $(CYGPATH_W) 'compat.c'; else $(CYGPATH_W) '$(srcdir)/compat.c'; fi`
	$(am__mv) $(DEPDIR)/spuunmux-compat.Tpo $(DEPDIR)/spuunmux-compat.Po
#	source='compat.c' object='spuunmux-compat.obj' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -c -o spuunmux-compat.obj `if test -f 'compat.c'; then $(CYGPATH_W) 'compat.c'; else $(CYGPATH_W) '$(srcdir)/compat.c'; fi`

spuunmux-conffile.o: conffile.c
	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -MT spuunmux-conffile.o -MD -MP -MF $(DEPDIR)/spuunmux-conffile.Tpo -c -o spuunmux-conffile.o `test -f 'conffile.c' || echo '$(srcdir)/'`conffile.c
	$(am__mv) $(DEPDIR)/spuunmux-conffile.Tpo $(DEPDIR)/spuunmux-conffile.Po
#	source='conffile.c' object='spuunmux-conffile.o' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -c -o spuunmux-conffile.o `test -f 'conffile.c' || echo '$(srcdir)/'`conffile.c

spuunmux-conffile.obj: conffile.c
	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -MT spuunmux-conffile.obj -MD -MP -MF $(DEPDIR)/spuunmux-conffile.Tpo -c -o spuunmux-conffile.obj `if test -f 'conffile.c'; then $(CYGPATH_W) 'conffile.c'; else $(CYGPATH_W) '$(srcdir)/conffile.c'; fi`
	$(am__mv) $(DEPDIR)/spuunmux-conffile.Tpo $(DEPDIR)/spuunmux-conffile.Po
#	source='conffile.c' object='spuunmux-conffile.obj' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(spuunmux_CFLAGS) $(CFLAGS) -c -o spuunmux-conffile.obj `if test -f 'conffile.c'; then $(CYGPATH_W) 'conffile.c'; else $(CYGPATH_W) '$(srcdir)/conffile.c'; fi`

ID: $(HEADERS) $(SOURCES) $(LISP) $(TAGS_FILES)
	list='$(SOURCES) $(HEADERS) $(LISP) $(TAGS_FILES)'; \
	unique=`for i in $$list; do \
	    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
	  done | \
	  $(AWK) '{ files[$$0] = 1; nonempty = 1; } \
	      END { if (nonempty) { for (i in files) print i; }; }'`; \
	mkid -fID $$unique
tags: TAGS

TAGS:  $(HEADERS) $(SOURCES) config.h.in $(TAGS_DEPENDENCIES) \
		$(TAGS_FILES) $(LISP)
	set x; \
	here=`pwd`; \
	list='$(SOURCES) $(HEADERS) config.h.in $(LISP) $(TAGS_FILES)'; \
	unique=`for i in $$list; do \
	    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
	  done | \
	  $(AWK) '{ files[$$0] = 1; nonempty = 1; } \
	      END { if (nonempty) { for (i in files) print i; }; }'`; \
	shift; \
	if test -z "$(ETAGS_ARGS)$$*$$unique"; then :; else \
	  test -n "$$unique" || unique=$$empty_fix; \
	  if test $$# -gt 0; then \
	    $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	      "$$@" $$unique; \
	  else \
	    $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	      $$unique; \
	  fi; \
	fi
ctags: CTAGS
CTAGS:  $(HEADERS) $(SOURCES) config.h.in $(TAGS_DEPENDENCIES) \
		$(TAGS_FILES) $(LISP)
	list='$(SOURCES) $(HEADERS) config.h.in $(LISP) $(TAGS_FILES)'; \
	unique=`for i in $$list; do \
	    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
	  done | \
	  $(AWK) '{ files[$$0] = 1; nonempty = 1; } \
	      END { if (nonempty) { for (i in files) print i; }; }'`; \
	test -z "$(CTAGS_ARGS)$$unique" \
	  || $(CTAGS) $(CTAGSFLAGS) $(AM_CTAGSFLAGS) $(CTAGS_ARGS) \
	     $$unique

GTAGS:
	here=`$(am__cd) $(top_builddir) && pwd` \
	  && $(am__cd) $(top_srcdir) \
	  && gtags -i $(GTAGS_ARGS) "$$here"

distclean-tags:
	-rm -f TAGS ID GTAGS GRTAGS GSYMS GPATH tags

distdir: $(DISTFILES)
	@srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	topsrcdirstrip=`echo "$(top_srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	list='$(DISTFILES)'; \
	  dist_files=`for file in $$list; do echo $$file; done | \
	  sed -e "s|^$$srcdirstrip/||;t" \
	      -e "s|^$$topsrcdirstrip/|$(top_builddir)/|;t"`; \
	case $$dist_files in \
	  */*) $(MKDIR_P) `echo "$$dist_files" | \
			   sed '/\//!d;s|^|$(distdir)/|;s,/[^/]*$$,,' | \
			   sort -u` ;; \
	esac; \
	for file in $$dist_files; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  if test -d $$d/$$file; then \
	    dir=`echo "/$$file" | sed -e 's,/[^/]*$$,,'`; \
	    if test -d "$(distdir)/$$file"; then \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -fpR $(srcdir)/$$file "$(distdir)$$dir" || exit 1; \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    cp -fpR $$d/$$file "$(distdir)$$dir" || exit 1; \
	  else \
	    test -f "$(distdir)/$$file" \
	    || cp -p $$d/$$file "$(distdir)/$$file" \
	    || exit 1; \
	  fi; \
	done
check-am: all-am
check: check-am
all-am: Makefile $(PROGRAMS) $(SCRIPTS) config.h
installdirs:
	for dir in "$(DESTDIR)$(bindir)" "$(DESTDIR)$(bindir)"; do \
	  test -z "$$dir" || $(MKDIR_P) "$$dir"; \
	done
install: install-am
install-exec: install-exec-am
install-data: install-data-am
uninstall: uninstall-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-am
install-strip:
	if test -z '$(STRIP)'; then \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	      install; \
	else \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	    "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'" install; \
	fi
mostlyclean-generic:
	-test -z "$(MOSTLYCLEANFILES)" || rm -f $(MOSTLYCLEANFILES)

clean-generic:

distclean-generic:
	-test -z "$(CONFIG_CLEAN_FILES)" || rm -f $(CONFIG_CLEAN_FILES)
	-test . = "$(srcdir)" || test -z "$(CONFIG_CLEAN_VPATH_FILES)" || rm -f $(CONFIG_CLEAN_VPATH_FILES)

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
	-test -z "$(MAINTAINERCLEANFILES)" || rm -f $(MAINTAINERCLEANFILES)
clean: clean-am

clean-am: clean-binPROGRAMS clean-generic mostlyclean-am

distclean: distclean-am
	-rm -rf ./$(DEPDIR)
	-rm -f Makefile
distclean-am: clean-am distclean-compile distclean-generic \
	distclean-hdr distclean-tags

dvi: dvi-am

dvi-am:

html: html-am

html-am:

info: info-am

info-am:

install-data-am:

install-dvi: install-dvi-am

install-dvi-am:

install-exec-am: install-binPROGRAMS install-nodist_binSCRIPTS

install-html: install-html-am

install-html-am:

install-info: install-info-am

install-info-am:

install-man:

install-pdf: install-pdf-am

install-pdf-am:

install-ps: install-ps-am

install-ps-am:

installcheck-am:

maintainer-clean: maintainer-clean-am
	-rm -rf ./$(DEPDIR)
	-rm -f Makefile
maintainer-clean-am: distclean-am maintainer-clean-generic

mostlyclean: mostlyclean-am

mostlyclean-am: mostlyclean-compile mostlyclean-generic

pdf: pdf-am

pdf-am:

ps: ps-am

ps-am:

uninstall-am: uninstall-binPROGRAMS uninstall-nodist_binSCRIPTS

.MAKE: all install-am install-strip

.PHONY: CTAGS GTAGS all all-am check check-am clean clean-binPROGRAMS \
	clean-generic ctags distclean distclean-compile \
	distclean-generic distclean-hdr distclean-tags distdir dvi \
	dvi-am html html-am info info-am install install-am \
	install-binPROGRAMS install-data install-data-am install-dvi \
	install-dvi-am install-exec install-exec-am install-html \
	install-html-am install-info install-info-am install-man \
	install-nodist_binSCRIPTS install-pdf install-pdf-am \
	install-ps install-ps-am install-strip installcheck \
	installcheck-am installdirs maintainer-clean \
	maintainer-clean-generic mostlyclean mostlyclean-compile \
	mostlyclean-generic pdf pdf-am ps ps-am tags uninstall \
	uninstall-am uninstall-binPROGRAMS uninstall-nodist_binSCRIPTS


# by having it depend on config.h, it will get rebuilt if ./configure is run
dvddirdel: $(srcdir)/dvddirdel.in config.h
	rm -f dvddirdel dvddirdel.tmp
	$(edit) $(srcdir)/dvddirdel.in > dvddirdel.tmp
	chmod +x dvddirdel.tmp
	mv dvddirdel.tmp dvddirdel

dvdvml.c: dvdvml.l
	$(FLEX) -s -B -Cem -o$@ -Pdvdvm $<

dvdvmy.c dvdvmy.h: dvdvmy.y
	$(BISON) -o dvdvmy.c -d -p dvdvm $<

dvdvml.o: dvdvmy.h

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
