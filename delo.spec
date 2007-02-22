%define		debver	0.8-2
%define		ver %(echo %{debver} | sed 's/-.*//')
Summary:	The DECstation boot loader
Name:		delo
Version:	%{ver}
Release:	0.1
License:	GPL
Group:		Applications/System
# debian? can't find original
Source0:	ftp://ftp.pl.debian.org/debian/pool/main/d/delo/%{name}_%{debver}.tar.gz
# Source0-md5:	c230e2c175a6488c7145b9a7118cc5ba
#URL:		
Provides:	bootloader
#ExclusiveArch:	mipsel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This is DELO, the DECstation boot loader, which you need to boot Linux
on DECstations from storage media. It can also create bootable media
for DECstations on other machines.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-boot,%{_mandir}/man{5,8}}

install delo/delo /sbin
install loader/delo.2nd /boot

install man/delo8 %{_mandir}/man8
install man/delo.conf.5 %{_mandir}/man5
install man/t-rex.1 %{_mandir}/man1

install t-rex/t-rex %{_bindir}
install t-rex-loader/t-rex-loader %{_libdir}/%{name}

install delo.conf /etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO kernel-patch/ramdisk_kernel_parameters.patch
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) /boot/delo.2nd
%attr(755,root,root) %{_sbindir}/delo
%attr(755,root,root) %{_bindir}/t-rex
%dir %attr(755,root,root) %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%{_mandir}/man[158]/*
