Summary:	Self-certifying File System (SFS)
Summary(pl):	System plików z Automatyczna certyfikacja(SFS)
Name:		sfs
Version:	0.5k
Release:	0.001
License:	LGPL
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Source0:	http://www.fs.net/download/%{name}-%{version}.tar.gz
BuildRequires:	gmp-devel
BuildRequires:	openssl-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SFS is a secure, global file system with completely decentralized
control. SFS lets you access your files from anywhere and share them
with anyone, anywhere. Anyone can set up an SFS server, and any user
can access any server from any client. SFS lets you share files across
administrative realms without involving administrators or
certification authorities.

%description -l pl
SFS jest bezpiecznym globalnym systemem plików z kompletnie
zdecentralizowan± kontrol±. Umo¿liwia Ci on dostêp do Twoich plików
sk±dkolwiek i wymienianie ich z kimkolwiek, gdziekolwiek. Ka¿dy mo¿e
ustawiæ serwer SFS i ka¿dy u¿ytkownik mo¿e pobieraæ/u¿ytkowaæ pliki z
ka¿dego serwera (ka¿dego klienta). SFS pozwala wymieniaæ pliki ponad
obszarami bez informowania administratorów lub organów autoryzuj±cych
certyfikaty.

%prep
%setup -q -n %{name}-0.5

%build
./configure --prefix=%{_prefix} \
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

%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
