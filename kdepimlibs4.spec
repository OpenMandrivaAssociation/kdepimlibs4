%define oname kdepimlibs

Summary:	Libraries of the KDE-PIM project
Name:		kdepimlibs4
Version:	4.14.10
Release:	4
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
%exclude %{_kde_bindir}/akonadi2xml
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
%{_kde_datadir}/config.kcfg/*
%{_kde_datadir}/mime/packages/kdepimlibs-mime.xml
%{_kde_datadir}/mime/packages/x-vnd.akonadi.socialfeeditem.xml
%{_kde_docdir}/HTML/en/kcontrol/kresources
%dir %{_kde_docdir}/HTML/en/kioslave

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}
Obsoletes:	%{_lib}mbox4 < 2:4.5.71

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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
Requires:	%{name}-core = %{EVRD}

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

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.13.2-1
- New version 4.13.2
- Drop no longer needed BuildRequires nepomuk-core-devel
- Update files

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-2
- Bump epoch because of moved libakonadi-xml subpackage

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1
- Some files were moved from kdepim4-runtime tarball here
- Move some files from akonadi-kde to kdepimlibs4-core
- Move libakonadi-xml subpackage here

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0

* Fri Jul 19 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-2
- Update BuildRequires

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-2
- Add Conflicts with choqok-devel for devel package to avoid file conflicts

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1
- Fix files

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0
- New subpackage libakonadi_socialutils
- Update files
- Add BuildRequires pkgconfig(QJson) and nepomuk-core-devel

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-2
- New version 4.9.0
- Re-diff l10n patch

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97
- Convert some BR to pkgconfig style

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- Update to 4.8.95

* Tue Jun 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.90-1
- Update to 4.8.90

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-1
- update to 4.8.3

* Mon Apr 16 2012 Mikhail Kompaniets <mkompan@mezon.ru> 2:4.8.2-2
- Russian localization for .desktop files

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762519
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758108
- New upstream tarball

* Sun Jan 01 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 748556
- New version

* Fri Dec 09 2011 Matthew Dawkins <mattydaw@mandriva.org> 2:4.7.90-1
+ Revision: 739525
- fixed BR for libxft-devel

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 731811
- New version 4.7.80

* Mon Aug 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 696071
- New version 4.7.41

* Thu Jul 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.40-1
+ Revision: 692008
- Fix file list
- New version 4.7.40

* Tue Jul 12 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.95-1
+ Revision: 689632
- New version 4.7Rc2

* Fri Jul 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.90-1
+ Revision: 689305
- New version kde 4.7rc1

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-1
+ Revision: 684409
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 2:4.6.3-1
+ Revision: 674013
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.2-1
+ Revision: 650779
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-1
+ Revision: 640731
- New version 4.6.1
- Add boost-devel as require of the devel package
  CCBUG: 62338

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.0-1
+ Revision: 632969
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.95-1mdv2011.0
+ Revision: 629125
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.90-1mdv2011.0
+ Revision: 624068
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.85-1mdv2011.0
+ Revision: 616349
- New upstream tarball

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 2:4.5.80-1mdv2011.0
+ Revision: 601420
- new version 4.5.80
- bump BR

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 2:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599098
- new snapshot 4.5.77

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1196755.1mdv2011.0
+ Revision: 597441
- new snapshot

* Sat Nov 13 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1196498.1mdv2011.0
+ Revision: 597207
- update snapshot to satisfy kdepim

* Sat Nov 13 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1196349.1mdv2011.0
+ Revision: 597032
- new snapshot 4.5.76

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 2:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589659
- new snapshot 4.5.74

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1183358.2mdv2011.0
+ Revision: 584289
- add includes to satisfy kdebindings
- obsoletes old mbox lib

* Thu Oct 07 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1183358.1mdv2011.0
+ Revision: 583974
- update file list
- New snapshot 4.5.71

* Tue Sep 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.68-1mdv2011.0
+ Revision: 578189
- New snapshot 4.5.68

* Thu Sep 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.67-1mdv2011.0
+ Revision: 575204
- New version 4.5.67

* Mon Aug 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.65-1mdv2011.0
+ Revision: 574550
- Fix file list
- New version kde 4.5.65

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-1mdv2011.0
+ Revision: 566573
- New upstream tarball
- Update to version 4.5.0

* Tue Jul 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.95-1mdv2011.0
+ Revision: 562111
- kde 4.4.95

* Tue Jul 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.92-1mdv2011.0
+ Revision: 561153
- Update to kde 4.5rc2

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-3mdv2010.1
+ Revision: 545887
- Rebuild in release mode

* Mon May 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-2mdv2010.1
+ Revision: 544913
- Add branch patch:
    - Don't include dots at the end of URLs in the URL highlighting.

* Wed May 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-1mdv2010.1
+ Revision: 542380
- Add branch patches
  Remove P301: Merged upstream
- Update to version 4.4.3

* Wed Apr 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-9mdv2010.1
+ Revision: 540291
- Add a patch fixing disribution list

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2:4.4.2-8mdv2010.1
+ Revision: 540238
- rebuild so that shared libraries are properly stripped again
- rebuild so that shared libraries are properly stripped again

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix patch header

* Sat Apr 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-6mdv2010.1
+ Revision: 536060
- Fix akonadi crash (BUG: 58812)

* Sat Apr 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-5mdv2010.1
+ Revision: 530883
- Add akonadi backport from trunk ( BKO: 222678 )

* Fri Apr 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-4mdv2010.1
+ Revision: 530760
- Add more akonadi trunk patches

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-3mdv2010.1
+ Revision: 528319
- Update to version 4.4.2

* Wed Mar 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-3mdv2010.1
+ Revision: 527113
- Fix version, remove subrel

* Wed Mar 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-2.1mdv2010.1
+ Revision: 527108
- Backport trunk patch for akonadi startup

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-1mdv2010.1
+ Revision: 513415
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-1mdv2010.1
+ Revision: 502616
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-1mdv2010.1
+ Revision: 498955
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-1mdv2010.1
+ Revision: 495699
- Update to kde 4.4 Rc2

* Sat Jan 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-1mdv2010.1
+ Revision: 488128
- fix conflicts because of libakonadi-kcal
- fix file list
- Update to 4.4 Rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-1mdv2010.1
+ Revision: 480577
- Update to kde 4.4 beta 2

* Thu Dec 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-1mdv2010.1
+ Revision: 472835
- Update to kde 4.4Beta1

* Thu Nov 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-1mdv2010.1
+ Revision: 470363
- Fix kdelibs4-devel require versionnate
- Update to kde 4.3.77
  Add branch switch for beta and final releases

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-1mdv2010.1
+ Revision: 466505
- Update to KDE 4.3.75
  Fix File list

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-4mdv2010.1
+ Revision: 465072
- Rebuild against new qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-3mdv2010.1
+ Revision: 462996
- Fix upgrade

* Fri Nov 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-2mdv2010.1
+ Revision: 461327
- Remove the requires for kdelibs4-experimental-devel
- Fix file list
- Update to kde 4.3.73

* Mon Oct 05 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-1mdv2010.0
+ Revision: 454025
- New upstream release 4.3.2.

* Thu Sep 24 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-2mdv2010.0
+ Revision: 448404
- Split all kioslaves cleaning out core package
- Remove wrong obsoletes in libraries
- Added conflicts to solve upgrade from 2009.1

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-1mdv2010.0
+ Revision: 423127
- New upstream release 4.3.1.

* Mon Aug 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.0-1mdv2010.0
+ Revision: 408607
- New upstream release 4.3.0.

* Thu Jul 23 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.98-1mdv2010.0
+ Revision: 398839
- Update to KDE 4.3 RC3

* Fri Jul 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.96-1mdv2010.0
+ Revision: 394236
- Update to Rc2

* Tue Jun 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-2mdv2010.0
+ Revision: 390780
- New tarball for Rc1

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-1mdv2010.0
+ Revision: 389069
- Fix file list
- Update to kde 4.3Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.90-1mdv2010.0
+ Revision: 382629
- Update to beta2

* Thu May 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.88-1mdv2010.0
+ Revision: 380641
- Update to kde 4.2.88

* Thu May 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.87-1mdv2010.0
+ Revision: 378301
- update to kde 4.2.87
- Add a switch to handle ftp snapshots

* Thu May 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-1mdv2010.0
+ Revision: 372994
- Fix Requires in kdelibs4
- Update to kde 4.2.85

* Mon May 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371493
- Update to kde 4.2.71

* Wed Apr 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 369151
- Update to kde 4.2.70

* Wed Apr 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-3mdv2009.1
+ Revision: 365229
- Add some upstream patches from branch
        - Patch101: Don't add [accept] etc when it's not an incidence as a freebusy mail

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-2mdv2009.1
+ Revision: 364173
- Remove old macros
  Add some upstream patches from branch
    - Patch100: Fix remove selected address

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-1mdv2009.1
+ Revision: 361618
- Upgrade to KDE 4.2.2 try#1 packages.

* Fri Feb 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-1mdv2009.1
+ Revision: 345562
- KDE 4.2.1 try#1 upstream release

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-2mdv2009.1
+ Revision: 340855
- Rebuild against qt4.5

* Mon Jan 26 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-1mdv2009.1
+ Revision: 333865
- Update with 4.2.0 upstream try#1 tarball
- Update with 4.2.0 upstream try#1 tarball

* Thu Jan 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-1mdv2009.1
+ Revision: 327252
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Tue Dec 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-2mdv2009.1
+ Revision: 317732
- Rebuild in debug mode

* Fri Dec 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-1mdv2009.1
+ Revision: 313753
- Fix File list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.85

* Wed Dec 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.82-1mdv2009.1
+ Revision: 312609
- Update to kde 4.1.82

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.81-1mdv2009.1
+ Revision: 308447
- Update to kde 4.1.81

* Wed Nov 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-1mdv2009.1
+ Revision: 304674
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-2mdv2009.1
+ Revision: 302946
- Add a missing require on a lib

* Thu Nov 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-1mdv2009.1
+ Revision: 302733
- Update to kde 4.1.73
- Add  buildrequires on libical ( will be a _must have_ for next kde snapshot)

* Thu Oct 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.71-1mdv2009.1
+ Revision: 296842
- New version 4.1.71

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.70-2mdv2009.1
+ Revision: 295844
- Fix Requires on libs

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.70-1mdv2009.1
+ Revision: 295460
- Add epoch because of new lib package which come from kdepim4
- Fix kdelibs4 required version
- Update to KDE 4.1.70
  libakonadi-kabc belong to this package now
  remove merged patches

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-3mdv2009.0
+ Revision: 289929
- Rebuild against new kde4-macros

* Sun Sep 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.2-2mdv2009.0
+ Revision: 289030
- [BUGFIX] fixes a very high CPU usage by KAlarm when there are alarms with sub-repetitions or deferrals with periods greater than 1 week. (Bug #44344)

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-1mdv2009.0
+ Revision: 288192
- KDE 4.1.2 arriving.

* Fri Sep 05 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-2mdv2009.0
+ Revision: 281247
- Regression fix for invitation mails

* Thu Aug 28 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-1mdv2009.0
+ Revision: 277080
- Upgrade to forthcoming 4.1.1 packages
- Daily branch update patches

* Tue Aug 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-4mdv2009.0
+ Revision: 271155
- Daily branch patch update

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-3mdv2009.0
+ Revision: 262896
- Update with current branch 4.1 patches

* Thu Jul 24 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-2mdv2009.0
+ Revision: 246266
- Update with Release Candidate 1 - 4.1.0
- Update with Release Candidate 1 - 4.1.0

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.98-1mdv2009.0
+ Revision: 233180
- Update with Release Candidate 1 - 4.0.98

* Sun Jul 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.85-1mdv2009.0
+ Revision: 232307
- Update to kde 4.0.85
  Remove patch0 : Merged upstream

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.84-2mdv2009.0
+ Revision: 229579
- Soname fix for gpgme libs

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.84-1mdv2009.0
+ Revision: 229433
- gpgme have new major
- Fix br
- Update with new snapshot tarballs 4.0.84

* Mon Jun 23 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.83-2mdv2009.0
+ Revision: 228469
- Latest hour package update with imap fixes

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.83-1mdv2009.0
+ Revision: 226081
- Update with new snapshot tarballs 4.0.83
- Update with new snapshot tarballs 4.0.82

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-2mdv2009.0
+ Revision: 218308
- Update with new snapshot tarballs 4.0.82
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.81-3mdv2009.0
+ Revision: 214701
- Update with new snapshot tarballs 4.0.81
- Update with new snapshot tarballs 4.0.81
- Update with new snapshot tarballs %%{VERSION}

* Thu May 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.81-1mdv2009.0
+ Revision: 213192
- New snapshot kde 4.0.81

* Sat May 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.80-1mdv2009.0
+ Revision: 210847
- Versionnate BuildRequires

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1
    - New upstream kde4 4.1 beta1

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.74-2mdv2009.0
+ Revision: 208120
- Rebuild because of BS failure
- Fix Requires
- Versionate buildRequires for akonadi

  + Funda Wang <fwang@mandriva.org>
    - BR automoc
    - New version 4.0.74

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.73-1mdv2009.0
+ Revision: 204495
- Remove unneeded Buildrequire
- Fix BuildRequires
- a new week, a new snapshot => 4.0.73

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.72-2mdv2009.0
+ Revision: 202257
- Fix Requires of kdepimlibs4-devel

* Thu May 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.72-1mdv2009.0
+ Revision: 199780
- Update to kde 4.0.72
- add akonadi-devel as BuildRequire
- bye bye libakonadi_protocolinternals
- New week-end New snapshot 4.0.70
- New snapshot 4.0.69
- New snapshot  4.0.68

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.3-1mdv2008.1
+ Revision: 190969
- Update for last stable release 4.0.3
- Update for last stable release 4.0.3
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.2-4mdv2008.1
+ Revision: 182124
- Rebuild against new qt4 changes
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.2-3mdv2008.1
+ Revision: 177368
- New upstream bugfix release 4.0.2
- Update for upstream upcoming 4.0.2

* Tue Feb 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.1-3mdv2008.1
+ Revision: 166355
- Rebuild

* Sun Feb 10 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-2mdv2008.1
+ Revision: 164754
- If you will change the sonames, remember the obsoletes

* Fri Feb 08 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-1mdv2008.1
+ Revision: 164269
- Fixed soname list
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE Team

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - ensure major correctness

* Thu Jan 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.0-1mdv2008.1
+ Revision: 147453
- remove a condition ( regroup )
  Enhance kdepimlibs4-core description

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update for final stable 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Dec 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.97.1-0.751976.1mdv2008.1
+ Revision: 137315
- new snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.97.1-0.746706.1mdv2008.1
+ Revision: 117051
- New snapshot

* Thu Dec 06 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.97.0-0.745183.1mdv2008.1
+ Revision: 115805
- Kde4 Rc2

* Thu Nov 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.742565.1mdv2008.1
+ Revision: 113975
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary

* Thu Nov 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.739809.1mdv2008.1
+ Revision: 111135
- New Snapshot

* Thu Nov 15 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.0-0.737106.1mdv2008.1
+ Revision: 108994
- Kde 4 RC1

* Sat Nov 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.2-0.734801.1mdv2008.1
+ Revision: 107435
+ rebuild (emptylog)

* Thu Nov 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.1-0.731416.1mdv2008.1
+ Revision: 104753
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.730641.2mdv2008.1
+ Revision: 103686
- New snapshot

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728852.2mdv2008.1
+ Revision: 101927
- New snapshot

* Wed Oct 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728683.2mdv2008.1
+ Revision: 101683
- New snapshot ( to allow to build kdebase )

* Tue Oct 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728203.2mdv2008.1
+ Revision: 101481
- Rebuild against new kdelibs

* Mon Oct 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728203.1mdv2008.1
+ Revision: 101309
- New svn snapshot

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.727394.1mdv2008.1
+ Revision: 101042
- New svn tarball

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.0-0.727394.1mdv2008.1
+ Revision: 100830
- New svn snapshot

* Wed Oct 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.0-0.726360.1mdv2008.1
+ Revision: 99734
- Use new snapshot tarball
- Kde 4 Beta 3

* Wed Oct 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.93.0-0.725942.1mdv2008.1
+ Revision: 99446
- New svn snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Fri Sep 28 2007 Tiago Salem <salem@mandriva.com.br> 3.93.0-0.714098.2mdv2008.0
+ Revision: 93624
- Removing mdv2008.0 from Obsoletes tags.

* Thu Sep 20 2007 Tiago Salem <salem@mandriva.com.br> 3.93.0-0.714098.1mdv2008.0
+ Revision: 91237
- Making Obsoletes tags versioned

* Fri Sep 14 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.712527.1mdv2008.0
+ Revision: 85735
- Update with revision 712527
- Proper file list
- Update with revision 711801
- kdepim4 moved ioslaves
- Update with revision 711783

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.708685.1mdv2008.0
+ Revision: 80477
- Update with revision 708685
- Update with revision 708685

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.708160.1mdv2008.0
+ Revision: 78993
- Update with revision 708160

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.706508.1mdv2008.0
+ Revision: 76085
- Update with revision 706508
- Update with revision 706508

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.706253.1mdv2008.0
+ Revision: 75033
- Update with revision 706253

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.705856.1mdv2008.0
+ Revision: 73299
- Update with revision 705856

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.705376.1mdv2008.0
+ Revision: 72359
- Update with revision 705376
- Update with revision 705376
- Update with revision 705307

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.704181.1mdv2008.0
+ Revision: 71059
- Update with revision 704181

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.702661.1mdv2008.0
+ Revision: 68483
- Update with revision 702661
- Update for revision 700869

* Tue Aug 14 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.699635.1mdv2008.0
+ Revision: 62941
- New upstream version 699635

* Thu Aug 09 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.698140.1mdv2008.0
+ Revision: 60926
- Update to revision 698140

* Thu Aug 02 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.695653.1mdv2008.0
+ Revision: 58267
- Update for revision 695653

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92-0.693061.1mdv2008.0
+ Revision: 56203
- Update for revision 693061

* Mon Jul 23 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.691459.1mdv2008.0
+ Revision: 54816
- Removed kleo library ( upstream )
- Renamed gpgmepp for gpgme++ ( upstream )
- Updated for revision 691459

* Fri Jul 20 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.690318.1mdv2008.0
+ Revision: 53994
- Update to revision 690318

* Wed Jul 18 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.689172.1mdv2008.0
+ Revision: 53138
- Fixed sonames again
- Update to revision 688639

* Wed Jul 11 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.686622.1mdv2008.0
+ Revision: 51413
- Update to revision 686622

* Wed Jul 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.686078.1mdv2008.0
+ Revision: 51213
- Fix File list
- New svn snapshot

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update revision 683847

* Tue Jul 03 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.682461.1mdv2008.0
+ Revision: 47497
- New snapshot
- New snaphot after BIC

* Thu Jun 28 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.681120.1mdv2008.0
+ Revision: 45392
- Update from svn for post 3.91

* Tue Jun 26 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.680386mdv2008.0
+ Revision: 44450
- Update for revision 680386

* Sat Jun 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.675772mdv2008.0
+ Revision: 40310
- Update for recent svn revision - 675772
- Update for recent svn revision

* Fri Jun 08 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.672993mdv2008.0
+ Revision: 37577
- New kdepimlibs4 package layout. follow new kdelibs.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix File list
    - New svn snapshot

* Wed May 09 2007 Laurent Montel <lmontel@mandriva.org> 3.90.1-0.20070502.1mdv2008.0
+ Revision: 25459
- Increase release
- new snapshot

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 3.80.3-0.20070502.3mdv2008.0
+ Revision: 20483
- new snapshot
- new snapshot


* Sat Apr 07 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070406.3mdv2007.1
+ Revision: 150897
- new snapshot
- Update
- new snapshot
- new snapshot
- new snapshot
- 3.80.3
- new snapshot
- new snapshot
- new snapshot

* Tue Jan 23 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070123.3mdv2007.1
+ Revision: 112262
- new snapshot

* Wed Jan 17 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070117.3mdv2007.1
+ Revision: 109747
- Update

* Tue Jan 09 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070109.3mdv2007.1
+ Revision: 106350
- Update snasphot

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070103.1mdv2007.1
+ Revision: 103521
- Minor fix
- Update from kde4 branch
  Fix spec files
- Use real release name

* Fri Dec 29 2006 Laurent Montel <lmontel@mandriva.com> 3.80-8mdv2007.1
+ Revision: 102473
- Add provides

* Thu Dec 28 2006 Laurent Montel <lmontel@mandriva.com> 3.80-7mdv2007.1
+ Revision: 102285
- Import kdepimlibs4

* Wed Dec 27 2006 Laurent Montel <lmontel@mandriva.com> 3.80-4mdv
- Update branch

* Tue Dec 19 2006 Laurent Montel <lmontel@mandriva.com> 3.80-1mdv
- First package

