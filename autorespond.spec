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
Scenariusz: poczta jest wysy³ana pod adres pomoc@moja-firma.com.
Automatycznie przygotowana odpowied¼ jest wysy³ana nadawcy z tego
w³a¶nie adresu. Mo¿esz równie¿ ustawiæ pusty adres nadawcy. Jednak
pamiêtaj, ¿e niektóre programy sprawdzaj± ten adres nadawcy, i je¿eli
jest on pusty, list mo¿e siê odbiæ, powoduj±c pêtlê.

Autoresponder sprawdza siê równie¿ w innych sytuacjach, takich jak:
listy od programu pocztowego, generowanie pustych nag³ówków koperty,
masowe pierwszeñstwo nag³ówków, itp.

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
