#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.12.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kanagram
Summary:	kanagram
Name:		ka6-%{kaname}
Version:	25.12.1
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fd2582117dd6eac5870066a82d02110e
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6OpenGL-devel
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Widgets-devel >= 5.11.1
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkeduvocdocument-devel >= %{version}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdeclarative-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt6MultimediaQuick
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kanagram is a game based on anagrams of words: the puzzle is solved
when the letters of the scrambled word are put back in the correct
order. There is no limit on either time taken, or the amount of
attempts to solve the word.

Features

• Several word lists included • Hints and cheat help system • Word
list editor • Word lists distribution via KNewStuff • Scalable user
interface appropriate for children

%description -l pl.UTF-8
Kanagram jest grą bazującą na anagramach słów; zagadka jest rozwiązana
gdy litery szukanego słowa są ustawione z powrotem w poprawnej
kolejności. Nie ma ograniczeń na wykorzystany czas ani na liczbę prób.

Właściwości

• Wiele list słów wbudowanych • System podpowiedzi • Edytor listy słów
• Dystrybucja listy słów przez KNewStuff • Skalowalny interfejs
użytkownika odpowiedni dla dzieci

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications/Games
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kanagram

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/org.kde.kanagram.desktop
%{_datadir}/config.kcfg/kanagram.kcfg
%{_iconsdir}/hicolor/128x128/apps/kanagram.png
%{_iconsdir}/hicolor/16x16/apps/kanagram.png
%{_iconsdir}/hicolor/24x24/apps/kanagram.png
%{_iconsdir}/hicolor/32x32/apps/kanagram.png
%{_iconsdir}/hicolor/48x48/apps/kanagram.png
%{_iconsdir}/hicolor/64x64/apps/kanagram.png
%{_iconsdir}/hicolor/80x80/apps/kanagram-harmattan.png
%{_iconsdir}/hicolor/scalable/apps/kanagram.svgz
%{_datadir}/kanagram
%{_datadir}/knsrcfiles/kanagram.knsrc
%{_datadir}/metainfo/org.kde.kanagram.appdata.xml
