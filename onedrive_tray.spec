Name:           onedrive-tray
Version:        1.0
Release:        1
Summary:        A simple tool to show a system tray icon and the OneDrive status

#Group:          Development/Languages
License:        Public Domain
URL:            https://github.com/DanielBorgesOliveira/onedrive_tray
Source0:        https://github.com/DanielBorgesOliveira/onedrive_tray/archive/refs/heads/master.zip
BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
Requires:       onedrive

%description
A simple tool to show a system tray icon and the OneDrive status

%build
unzip -d ./ %{SOURCE0}
cd onedrive_tray-master
mkdir -p build
cd build
qmake-qt5 ../systray.pro
make

%install
# Get Qt5 translation dir
%define qt_trans_dir %(qmake-qt5 -query QT_INSTALL_TRANSLATIONS)

mkdir -p %{buildroot}/usr/bin/
install -m 755 ./onedrive_tray-master/build/onedrive_tray -t %{buildroot}/usr/bin/
mkdir -p %{buildroot}%{qt_trans_dir}
install -m 644 ./onedrive_tray-master/onedrive_tray_*.qm -t %{buildroot}%{qt_trans_dir}
mkdir -p %{buildroot}/usr/lib/systemd/system/
install -m 644 ./onedrive_tray-master/onedrive_tray.service -t %{buildroot}/usr/lib/systemd/system/

%post -p /usr/bin/bash
systemctl daemon-reload

%files
/usr/bin/onedrive_tray
/usr/lib/systemd/system/onedrive_tray.service
%{qt_trans_dir}/onedrive_tray_de.qm
%{qt_trans_dir}/onedrive_tray_en.qm
%{qt_trans_dir}/onedrive_tray_es.qm
%{qt_trans_dir}/onedrive_tray_fr.qm
%{qt_trans_dir}/onedrive_tray_nl.qm

%changelog
* Thu Aug 18 2022 Michael Schlapa <michael@schlapa.eu>
- 1.0-1 Initial package

