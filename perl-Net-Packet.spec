%define upstream_name	 Net-Packet
%define upstream_version 3.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A framework to easily send and receive frames from layer 2 to layer 7
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	chrpath
BuildRequires:	pcap-devel
BuildRequires:	perl(Bit::Vector)
BuildRequires:	perl(Class::Gomor::Hash)
BuildRequires:	perl(IO::Interface)
BuildRequires:	perl(Net::IPv6Addr)
BuildRequires:	perl(Net::Libdnet)
BuildRequires:	perl(Net::Pcap)
BuildRequires:	perl(Net::Write)
BuildRequires:	perl(Socket6)
BuildRequires:	perl-devel

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

# this won't work, but partly works as root...
#make test

%install
%makeinstall_std

%files
%doc Changes README examples
%{perl_vendorlib}/Net
%{_mandir}/*/*

%changelog
* Tue Nov 10 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.270.0-1mdv2010.1
+ Revision: 463921
- update to 3.27

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.260.0-1mdv2010.0
+ Revision: 404111
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.26-2mdv2009.0
+ Revision: 268625
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-1mdv2009.0
+ Revision: 196163
- update to new version 3.26

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 3.25-2mdv2008.1
+ Revision: 152224
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 3.25-1mdv2008.0
+ Revision: 20670
- 3.25


* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.22-1mdk
- New release 2.22

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.20-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Wed Mar 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.20-2mdk
- re-add URL I wronly removed in previous build

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.20-1mdk
- New release 2.20
- drop patch

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-1mdk
- New release 2.06
- spec cleanup

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.04-1mdk
- initial Mandriva package

