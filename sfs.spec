Summary:	Self-certifying File System (SFS)
Summary(pl.UTF-8):	System plików z Automatyczna certyfikacja (SFS)
Name:		sfs
Version:	0.7.2
Release:	0.1
License:	LGPL
Group:		Base/Kernel
Source0:	http://www.fs.net/sfswww/dist/%{name}-%{version}.tar.gz
# Source0-md5:	1fb559f144c4d367ef01e93beb1dea1e
BuildRequires:	gmp-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SFS is a secure, global file system with completely decentralized
control. SFS lets you access your files from anywhere and share them
with anyone, anywhere. Anyone can set up an SFS server, and any user
can access any server from any client. SFS lets you share files across
administrative realms without involving administrators or
certification authorities.

%description -l pl.UTF-8
SFS jest bezpiecznym globalnym systemem plików z kompletnie
zdecentralizowaną kontrolą. Umożliwia Ci on dostęp do Twoich plików
skądkolwiek i wymienianie ich z kimkolwiek, gdziekolwiek. Każdy może
ustawić serwer SFS i każdy użytkownik może pobierać/użytkować pliki z
każdego serwera (każdego klienta). SFS pozwala wymieniać pliki ponad
obszarami bez informowania administratorów lub organów autoryzujących
certyfikaty.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--enable-shlib \
	--enable-shared \
	--enable-static \
	--with-gmp=%{_prefix} \
	--with-openssl=%{_prefix} \
	--with-db3 \
	--enable-uvfs \
	--enable-repo \
	--with-etcdir=%{_sysconfdir} \
	--with-sfsdir=%{_prefix} \
	--with-sfsuser=sfs \
	--with-sfsgroup=sfs

%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
