# NOTE: this package is obsolete. Use texlive-latexdiff instead.

Summary:	Determine and mark up significant differences between latex files
Name:		latexdiff
Version:	1.3.4
Release:	1
URL:		https://ctan.org/pkg/latexdiff
Source:		https://mirrors.ctan.org/support/latexdiff.zip
License:	GPLv2
Group:		Text tools
Requires:	tex(latex)

BuildArch: noarch

%description
Latexdiff is a Perl script for visual mark up and revision of
significant differences between two latex files.  Various options are
available for visual markup using standard latex packages such as
color.  Changes not directly affecting visible text, for example in
formatting commands, are still marked in the latex source.  A
rudimentary revision facility is provided by another Perl script,
latexrevise, which accepts or rejects all changes.  Manual editing of
the difference file can be used to override this default behaviour and
accept or reject selected changes only.

%files
%license COPYING
%doc doc/* example
%{_bindir}/latexdiff
%{_bindir}/latexdiff-fast
%{_bindir}/latexdiff-so
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise
%{_mandir}/man1/latexdiff.1*
%{_mandir}/man1/latexdiff-vc.1*
%{_mandir}/man1/latexrevise.1*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n latexdiff

%build

%install
install -pm 0755 -d %{buildroot}/%{_bindir}
install -pm 0755 latexdiff latexdiff-fast latexdiff-so latexdiff-vc latexrevise %{buildroot}/%{_bindir}

install -pm 0755 -d %{buildroot}/%{_mandir}/man1
install -pm 0644 *.1 %{buildroot}/%{_mandir}/man1

