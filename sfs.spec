Summary:	Self-certifying File System
Summary(pl):	
Name:		sfs
Version:	0.5k
Release:	0.001
Copyright:	LGPL
Group:		/base/kernel
Source0:	http://www.fs.net/download/%{name}-%{version}.tar.gz
BuildRequires:	gmp-devel
BuildRequires:	openssl-devel
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
SFS is a secure, global file system with completely decentralized control. 
SFS lets you access your files from anywhere and share them with anyone, 
anywhere. Anyone can set up an SFS server, and any user can access any 
server from any client. SFS lets you share files across administrative 
realms without involving administrators or certification authorities. 

%description -l pl

%prep
%setup -q -n %{name}-0.5

#%patch

%build
./configure --prefix=%{_prefix} \
	--enable-shlib \
	--enable-shared \
	--enable-static \
	--with-gmp=%{_prefix} \
	--with-openssl=%{_prefix} \
	--with-db3 \
	--enable-uvfs \
	--with-etcdir=%{_sysconfdir} \
	--with-sfsdir=%{_prefix} \
	--with-sfsuser=sfs \
	--with-sfsgroup=sfs

%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
