Summary:	Simple autoresponder for qmail
Summary(pl):	Prosty autoresponder dla qmaila
Name:		autorespond
Version:	2.0.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.inter7.com/devel/%{name}-%{version}.tar.gz
# Source0-md5:	aa81f2c02b36ccd3ce58c60f0f89683e
URL:		http://inter7.com/qmailadmin/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail is sent to help@my-company.com. An automatically generated
response is sent back to the user with an address of
"help@my-company.com". You can set the envelope sender to an empty
string. However, some programs will parse the message for the "From:"
field and send an autoresponse back to it. It is received at your
autoresponder, and you now have a mail loop.

This autoresponder also catches some other simple situations such as
mail from a mailer-daemon, empty envelope sender, bulk precedence
headers, etc.

%description -l pl
Scenariusz: poczta jest wysy�ana pod adres pomoc@moja-firma.com.
Automatycznie przygotowana odpowied� jest wysy�ana nadawcy z tego
w�a�nie adresu. Mo�esz r�wnie� ustawi� pusty adres nadawcy. Jednak
pami�taj, �e niekt�re programy sprawdzaj� ten adres nadawcy, i je�eli
jest on pusty, list mo�e si� odbi�, powoduj�c p�tl�.

Autoresponder sprawdza si� r�wnie� w innych sytuacjach, takich jak:
listy od programu pocztowego, generowanie pustych nag��wk�w koperty,
masowe pierwsze�stwo nag��wk�w, itp.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -D_REENTRANT" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README help_message qmail-auto
%attr(755,root,root) %{_bindir}/*
