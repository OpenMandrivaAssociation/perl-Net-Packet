%define upstream_name	 Net-Packet
%define upstream_version 3.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A framework to easily send and receive frames from layer 2 to layer 7
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	chrpath
BuildRequires:	libpcap-devel
BuildRequires:	perl-Class-Gomor-Hash >= 0.20
BuildRequires:	perl(IO::Interface)
BuildRequires:	perl(Net::IPv6Addr)
BuildRequires:	perl-Net-Pcap >= 0.04
BuildRequires:	perl(Socket6)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a unified framework to craft, send and receive
packets at layers 2, 3, 4 and 7.  Basically, you forge each layer
of a frame (Net::Packet::IPv4 for layer 3, Net::Packet::TCP for
layer 4 ; for example), and pack all of this into a
Net::Packet::Frame object. Then, you can send the frame to the
network, and receive it easily, since the response is
automatically searched for and matched against the request.  If
you want some layer 2, 3 or 4 protocol encoding/decoding to be
added, just ask, and give a corresponding .pcap file ;)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

# this won't work, but partly works as root...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

# nuke rpath
find %{buildroot} -name "*.so" | xargs chrpath -d

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples
%{perl_vendorlib}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/*/*
