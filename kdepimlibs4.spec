%define oname kdepimlibs

Summary:	Libraries of the KDE-PIM project
Name:		kdepimlibs4
Version:	4.14.10
Release:	8
Epoch:		3
Group:		Graphical desktop/KDE
License:	ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
Url:		https://projects.kde.org/projects/kde/kdepimlibs
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/14.12.2/src/%{oname}-%{version}.tar.xz
Patch1:		kdepimlibs-4.14.10-dont-build-tests.patch
BuildRequires:	automoc4
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xpm)

%description
This module includes libraries that are central to the development and
execution of a KDE-PIM application.

The KDE-PIM project aims to bring together those who wish to help design,
implement, test, etc. anything that's to do with personal information
management.

This rather broad scope encompasses mail clients, addressbooks, usenet news,
scheduling and even sticky notes.

#----------------------------------------------------------------------------

%package core
Group:		Development/KDE and Qt
Summary:	Config file and icons file for %{name}
Obsoletes:	kdepimlibs4-common < %{EVRD}
Obsoletes:	kdepim4-ioslaves < %{EVRD}
Conflicts:	%{name}-devel < 2.4.5.71
Conflicts:	akonadi-kde < 3:4.12.0

%description core
This packages contains all icons, config file etc... of kdepimlibs4.

%files core
%{_kde_libdir}/kde4/akonadi_serializer_socialfeeditem.so
%{_kde_libdir}/kde4/kabc_directory.so
%{_kde_libdir}/kde4/kabc_file.so
%{_kde_libdir}/kde4/kabc_net.so
%{_kde_libdir}/kde4/kabcformat_binary.so
%{_kde_libdir}/kde4/kcal_local.so
%{_kde_libdir}/kde4/kcal_localdir.so
%{_kde_libdir}/kde4/kcm_akonadicontact_actions.so
%{_kde_libdir}/kde4/kcm_kresources.so
%{_kde_libdir}/kde4/kcm_mailtransport.so
%{_kde_appsdir}/akonadi/
%{_kde_appsdir}/akonadi-kde/
%{_kde_appsdir}/kabc/
%{_kde_appsdir}/kconf_update/mailtransports.upd
%{_kde_appsdir}/kconf_update/migrate-transports.pl
%{_kde_appsdir}/libkholidays/
%{_kde_services}/akonadi/contact
%{_kde_services}/akonadicontact_actions.desktop
%{_kde_services}/kcm_mailtransport.desktop
%dir %{_kde_services}/kresources
%{_kde_services}/kresources.desktop
%dir %{_kde_services}/kresources/kabc
%{_kde_services}/kresources/kabc/dir.desktop
%{_kde_services}/kresources/kabc/file.desktop
%{_kde_services}/kresources/kabc/net.desktop
%{_kde_services}/kresources/kabc_manager.desktop
%{_kde_services}/kresources/kcal
%{_kde_services}/kresources/kcal_manager.desktop
%{_kde_servicetypes}/*.desktop
%{_datadir}/dbus-1/interfaces/*
%{_kde_datadir}/mime/packages/kdepimlibs-mime.xml
%{_kde_datadir}/mime/packages/x-vnd.akonadi.socialfeeditem.xml
%dir %{_kde_docdir}/HTML/en/kioslave
%{_kde_docdir}/HTML/en/kcontrol/kresources

#----------------------------------------------------------------------------

%package -n kio4-imap
Summary:	KDE 4 imap module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-imap
KDE 4 imap module.

%files -n kio4-imap
%{_kde_docdir}/HTML/en/kioslave/imap
%{_kde_libdir}/kde4/kio_imap4.so
%{_kde_datadir}/kde4/services/imap*

#----------------------------------------------------------------------------

%package -n kio4-pop3
Summary:	KDE 4 pop3 module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-pop3
KDE 4 pop3 module.

%files -n kio4-pop3
%{_kde_docdir}/HTML/en/kioslave/pop3
%{_kde_libdir}/kde4/kio_pop3.so
%{_kde_datadir}/kde4/services/pop*

#----------------------------------------------------------------------------

%package -n kio4-ldap
Summary:	KDE 4 ldap module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-ldap
KDE 4 ldap module.

%files -n kio4-ldap
%{_kde_docdir}/HTML/en/kioslave/ldap
%{_kde_libdir}/kde4/kio_ldap.so
%{_kde_datadir}/kde4/services/ldap*
%{_kde_libdir}/kde4/kabc_ldapkio.so
%{_kde_datadir}/kde4/services/kresources/kabc/ldapkio.desktop

#----------------------------------------------------------------------------

%package -n kio4-sieve
Summary:	KDE 4 sieve module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-sieve
KDE 4 sieve module.

%files -n kio4-sieve
%{_kde_libdir}/kde4/kio_sieve.so
%{_kde_datadir}/kde4/services/sieve*
%doc %{_kde_docdir}/HTML/en/kioslave/sieve

#----------------------------------------------------------------------------

%package -n kio4-mbox
Summary:	KDE 4 mbox module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-mbox
KDE 4 mbox module.

%files -n kio4-mbox
%{_kde_libdir}/kde4/kio_mbox.so
%{_kde_datadir}/kde4/services/mbox*
%doc %{_kde_docdir}/HTML/en/kioslave/mbox

#----------------------------------------------------------------------------

%package -n kio4-smtp
Summary:	KDE 4 smtp module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-smtp
KDE 4 smtp module.

%files -n kio4-smtp
%{_kde_docdir}/HTML/en/kioslave/smtp
%{_kde_libdir}/kde4/kio_smtp.so
%{_kde_datadir}/kde4/services/smtp*

#----------------------------------------------------------------------------

%package -n kio4-nntp
Summary:	KDE 4 nntp module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio4-nntp
KDE 4 nntp module.

%files -n kio4-nntp
%{_kde_docdir}/HTML/en/kioslave/nntp
%{_kde_libdir}/kde4/kio_nntp.so
%{_kde_datadir}/kde4/services/nntp*

#----------------------------------------------------------------------------

%define akonadi_calendar_major 4
%define libakonadi_calendar %mklibname akonadi-calendar %{akonadi_calendar_major}

%package -n %{libakonadi_calendar}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_calendar}
KDE 4 core library.

%files -n %{libakonadi_calendar}
%{_kde_libdir}/libakonadi-calendar.so.%{akonadi_calendar_major}*

#----------------------------------------------------------------------------

%define akonadi_contact_major 4
%define libakonadi_contact %mklibname akonadi-contact %{akonadi_contact_major}

%package -n %{libakonadi_contact}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_contact}
KDE 4 core library.

%files -n %{libakonadi_contact}
%{_kde_libdir}/libakonadi-contact.so.%{akonadi_contact_major}*

#----------------------------------------------------------------------------

%define akonadi_kabc_major 4
%define libakonadi_kabc %mklibname akonadi-kabc %{akonadi_kabc_major}

%package -n %{libakonadi_kabc}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_kabc}
KDE 4 core library.

%files -n %{libakonadi_kabc}
%{_kde_libdir}/libakonadi-kabc.so.%{akonadi_kabc_major}*

#----------------------------------------------------------------------------

%define akonadi_kcal_major 4
%define libakonadi_kcal %mklibname akonadi-kcal %{akonadi_kcal_major}

%package -n %{libakonadi_kcal}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_kcal}
KDE 4 core library.

%files -n %{libakonadi_kcal}
%{_kde_libdir}/libakonadi-kcal.so.%{akonadi_kcal_major}*

#----------------------------------------------------------------------------

%define akonadi_kde_major 4
%define libakonadi_kde %mklibname akonadi-kde %{akonadi_kde_major}

%package -n %{libakonadi_kde}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_kde}
KDE 4 core library.

%files -n %{libakonadi_kde}
%{_kde_libdir}/libakonadi-kde.so.%{akonadi_kde_major}*

#----------------------------------------------------------------------------

%define akonadi_kmime_major 4
%define libakonadi_kmime %mklibname akonadi-kmime %{akonadi_kmime_major}

%package -n %{libakonadi_kmime}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_kmime}
KDE 4 core library.

%files -n %{libakonadi_kmime}
%{_kde_libdir}/libakonadi-kmime.so.%{akonadi_kmime_major}*

#----------------------------------------------------------------------------

%define akonadi_notes_major 4
%define libakonadi_notes %mklibname akonadi-notes %{akonadi_notes_major}

%package -n %{libakonadi_notes}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libakonadi_notes}
KDE 4 core library.

%files -n %{libakonadi_notes}
%{_kde_libdir}/libakonadi-notes.so.%{akonadi_notes_major}*

#----------------------------------------------------------------------------

%define akonadi_socialutils_major 4
%define libakonadi_socialutils %mklibname akonadi-socialutils %{akonadi_socialutils_major}

%package -n %{libakonadi_socialutils}
Summary:	Akonadi social utilities library
Group:		System/Libraries

%description -n %{libakonadi_socialutils}
Akonadi social utilities library.

%files -n %{libakonadi_socialutils}
%{_kde_libdir}/libakonadi-socialutils.so.%{akonadi_socialutils_major}*

#-----------------------------------------------------------------------------

%define akonadi_xml_major 4
%define libakonadi_xml %mklibname akonadi-xml %{akonadi_xml_major}

%package -n %{libakonadi_xml}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakonadi_xml}
KDE 4 library.

%files -n %{libakonadi_xml}
%{_kde_libdir}/libakonadi-xml.so.%{akonadi_xml_major}*

#----------------------------------------------------------------------------

%define kabc_major 4
%define libkabc %mklibname kabc %{kabc_major}

%package -n %{libkabc}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkabc}
KDE 4 core library.

%files -n %{libkabc}
%{_kde_libdir}/libkabc.so.%{kabc_major}*

#----------------------------------------------------------------------------

%define kblog_major 4
%define libkblog %mklibname kblog %{kblog_major}

%package -n %{libkblog}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkblog}
KDE 4 core library.

%files -n %{libkblog}
%{_kde_libdir}/libkblog.so.%{kblog_major}*

#----------------------------------------------------------------------------

%define kabc_file_core_major 4
%define libkabc_file_core %mklibname kabc_file_core %{kabc_file_core_major}

%package -n %{libkabc_file_core}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkabc_file_core}
KDE 4 core library.

%files -n %{libkabc_file_core}
%{_kde_libdir}/libkabc_file_core.so.%{kabc_file_core_major}*

#----------------------------------------------------------------------------

%define kcal_major 4
%define libkcal %mklibname kcal %{kcal_major}

%package -n %{libkcal}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkcal}
KDE 4 core library.

%files -n %{libkcal}
%{_kde_libdir}/libkcal.so.%{kcal_major}*

#----------------------------------------------------------------------------

%define kimap_major 4
%define libkimap %mklibname kimap %{kimap_major}

%package -n %{libkimap}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkimap}
KDE 4 core library.

%files -n %{libkimap}
%{_kde_libdir}/libkimap.so.%{kimap_major}*

#----------------------------------------------------------------------------

%define kldap_major 4
%define libkldap %mklibname kldap %{kldap_major}

%package -n %{libkldap}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkldap}
KDE 4 core library.

%files -n %{libkldap}
%{_kde_libdir}/libkldap.so.%{kldap_major}*

#----------------------------------------------------------------------------

%define kmbox_major 4
%define libkmbox %mklibname kmbox %{kmbox_major}

%package -n %{libkmbox}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkmbox}
KDE 4 core library.

%files -n %{libkmbox}
%{_kde_libdir}/libkmbox.so.%{kmbox_major}*

#----------------------------------------------------------------------------

%define kmime_major 4
%define libkmime %mklibname kmime %{kmime_major}

%package -n %{libkmime}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkmime}
KDE 4 core library.

%files -n %{libkmime}
%{_kde_libdir}/libkmime.so.%{kmime_major}*

#----------------------------------------------------------------------------

%define kpimutils_major 4
%define libkpimutils %mklibname kpimutils %{kpimutils_major}

%package -n %{libkpimutils}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkpimutils}
KDE 4 core library.

%files -n %{libkpimutils}
%{_kde_libdir}/libkpimutils.so.%{kpimutils_major}*

#----------------------------------------------------------------------------

%define kresources_major 4
%define libkresources %mklibname kresources %{kresources_major}

%package -n %{libkresources}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkresources}
KDE 4 core library.

%files -n %{libkresources}
%{_kde_libdir}/libkresources.so.%{kresources_major}*

#----------------------------------------------------------------------------

%define ktnef_major 4
%define libktnef %mklibname ktnef %{ktnef_major}

%package -n %{libktnef}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libktnef}
KDE 4 core library.

%files -n %{libktnef}
%{_kde_libdir}/libktnef.so.%{ktnef_major}*

#----------------------------------------------------------------------------

%define kxmlrpcclient_major 4
%define libkxmlrpcclient %mklibname kxmlrpcclient %{kxmlrpcclient_major}

%package -n %{libkxmlrpcclient}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkxmlrpcclient}
KDE 4 core library.

%files -n %{libkxmlrpcclient}
%{_kde_libdir}/libkxmlrpcclient.so.%{kxmlrpcclient_major}*

#----------------------------------------------------------------------------

%define mailtransport_major 4
%define libmailtransport %mklibname mailtransport %{mailtransport_major}

%package -n %{libmailtransport}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libmailtransport}
KDE 4 core library.

%files -n %{libmailtransport}
%{_kde_libdir}/libmailtransport.so.%{mailtransport_major}*

#------------------------------------------------

%define syndication_major 4
%define libsyndication %mklibname syndication %{syndication_major}

%package -n %{libsyndication}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libsyndication}
KDE 4 core library.

%files -n %{libsyndication}
%{_kde_libdir}/libsyndication.so.%{syndication_major}*

#----------------------------------------------------------------------------

%define qgpgme_major 1
%define libqgpgme %mklibname qgpgme %{qgpgme_major}

%package -n %{libqgpgme}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libqgpgme}
KDE 4 core library.

%files -n %{libqgpgme}
%{_kde_libdir}/libqgpgme.so.%{qgpgme_major}*

#----------------------------------------------------------------------------

%define gpgmepp_major 2
%define libgpgmepp %mklibname gpgme++ %{gpgmepp_major}

%package -n %{libgpgmepp}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libgpgmepp}
KDE 4 core library.

%files -n %{libgpgmepp}
%{_kde_libdir}/libgpgme+*.so.%{gpgmepp_major}*

#----------------------------------------------------------------------------

%define kpimidentities_major 4
%define libkpimidentities %mklibname kpimidentities %{kpimidentities_major}

%package -n %{libkpimidentities}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkpimidentities}
KDE 4 core library.

%files -n %{libkpimidentities}
%{_kde_libdir}/libkpimidentities.so.%{kpimidentities_major}*

#----------------------------------------------------------------------------

%define kholidays_major 4
%define libkholidays %mklibname kholidays %{kholidays_major}

%package -n %{libkholidays}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkholidays}
KDE 4 core library.

%files -n %{libkholidays}
%{_kde_libdir}/libkholidays.so.%{kholidays_major}*

#----------------------------------------------------------------------------

%define kpimtextedit_major 4
%define libkpimtextedit %mklibname kpimtextedit %{kpimtextedit_major}

%package -n %{libkpimtextedit}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkpimtextedit}
KDE 4 core library.

%files -n %{libkpimtextedit}
%{_kde_libdir}/libkpimtextedit.so.%{kpimtextedit_major}*

#----------------------------------------------------------------------------

%define microblog_major 4
%define libmicroblog %mklibname microblog %{microblog_major}

%package -n %{libmicroblog}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libmicroblog}
KDE 4 core library.

%files -n %{libmicroblog}
%{_kde_libdir}/libmicroblog.so.%{microblog_major}*

#----------------------------------------------------------------------------

%define kontactinterface_major 4
%define libkontactinterface %mklibname kontactinterface %{kontactinterface_major}

%package -n %{libkontactinterface}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkontactinterface}
KDE 4 core library.

%files -n %{libkontactinterface}
%{_kde_libdir}/libkontactinterface.so.%{kontactinterface_major}*

#----------------------------------------------------------------------------

%define kcalcore_major 4
%define libkcalcore %mklibname kcalcore %{kcalcore_major}

%package -n %{libkcalcore}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkcalcore}
KDE 4 core library.

%files -n %{libkcalcore}
%{_kde_libdir}/libkcalcore.so.%{kcalcore_major}*

#----------------------------------------------------------------------------

%define kcalutils_major 4
%define libkcalutils %mklibname kcalutils %{kcalutils_major}

%package -n %{libkcalutils}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkcalutils}
KDE 4 core library.

%files -n %{libkcalutils}
%{_kde_libdir}/libkcalutils.so.%{kcalutils_major}*

#----------------------------------------------------------------------------

%define kalarmcal_major 2
%define libkalarmcal %mklibname kalarmcal %{kalarmcal_major}

%package -n %{libkalarmcal}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkalarmcal}
KDE 4 core library.

%files -n %{libkalarmcal}
%{_kde_libdir}/libkalarmcal.so.%{kalarmcal_major}*

#----------------------------------------------------------------------------

%package devel
Group:		Development/KDE and Qt
Summary:	Header files and documentation for compiling KDE applications
Requires:	%{name}-core = %{EVRD}
Requires:	%{libakonadi_calendar} = %{EVRD}
Requires:	%{libakonadi_contact} = %{EVRD}
Requires:	%{libakonadi_kabc} = %{EVRD}
Requires:	%{libakonadi_kcal} = %{EVRD}
Requires:	%{libakonadi_kde} = %{EVRD}
Requires:	%{libakonadi_kmime} = %{EVRD}
Requires:	%{libakonadi_notes} = %{EVRD}
Requires:	%{libakonadi_socialutils} = %{EVRD}
Requires:	%{libakonadi_xml} = %{EVRD}
Requires:	%{libgpgmepp} = %{EVRD}
Requires:	%{libkabc} = %{EVRD}
Requires:	%{libkabc_file_core} = %{EVRD}
Requires:	%{libkblog} = %{EVRD}
Requires:	%{libkcal} = %{EVRD}
Requires:	%{libkcalcore} = %{EVRD}
Requires:	%{libkcalutils} = %{EVRD}
Requires:	%{libkholidays} = %{EVRD}
Requires:	%{libkimap} = %{EVRD}
Requires:	%{libkldap} = %{EVRD}
Requires:	%{libkmbox} = %{EVRD}
Requires:	%{libkmime} = %{EVRD}
Requires:	%{libkontactinterface} = %{EVRD}
Requires:	%{libkpimidentities} = %{EVRD}
Requires:	%{libkpimtextedit} = %{EVRD}
Requires:	%{libkpimutils} = %{EVRD}
Requires:	%{libkresources} = %{EVRD}
Requires:	%{libktnef} = %{EVRD}
Requires:	%{libkxmlrpcclient} = %{EVRD}
Requires:	%{libmailtransport} = %{EVRD}
Requires:	%{libmicroblog} = %{EVRD}
Requires:	%{libqgpgme} = %{EVRD}
Requires:	%{libsyndication} = %{EVRD}
Requires:	%{libkalarmcal} = %{EVRD}
Requires:	kdelibs-devel
Requires:	boost-devel
# To avoid file conflict (FindQtOAuth.cmake)
Conflicts:	choqok-devel < 1.3-3

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_kde_datadir}/apps/cmake/*/*
%{_kde_libdir}/gpgmepp/*.cmake
%{_kde_libdir}/kde4/plugins/designer/*.so
%{_kde_libdir}/cmake/KdepimLibs

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%apply_patches
# required for cmake now
sed -i '1s/^/cmake_minimum_required(VERSION 2.4)\n/' CMakeLists.txt

%build
%cmake_kde4 -DKDE4_BUILD_TESTS=OFF
%make

%install
%makeinstall_std -C build

# dont want this
rm -f %{buildroot}/%{_kde_bindir}/akonadi2xml

# (tpg) remove this as it conflicts with kmailtransport package
rm -rf %{buildroot}%{_datadir}/config.kcfg/mailtransport.kcfg

# (tpg) remove these as them are not needed
rm -rf %{buildroot}%{_datadir}/config.kcfg/recentcontactscollections.kcfg
rm -rf %{buildroot}%{_datadir}/config.kcfg/resourcebase.kcfg
rm -rf %{buildroot}%{_datadir}/config.kcfg/specialmailcollections.kcfg

