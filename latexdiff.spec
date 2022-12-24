Summary:	Determine and mark up significant differences between latex files
Name:		latexdiff
Version:	1.3.3
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
%defattr(-,root,root,-)
%doc doc/* example
%attr(755,root,root) %{_bindir}/latexdiff
%attr(755,root,root) %{_bindir}/latexdiff-fast
%attr(755,root,root) %{_bindir}/latexdiff-so
%attr(755,root,root) %{_bindir}/latexdiff-vc
%attr(755,root,root) %{_bindir}/latexrevise
%attr(644,root,root) %{_mandir}/man1/latexdiff.1*
%attr(644,root,root) %{_mandir}/man1/latexdiff-vc.1*
%attr(644,root,root) %{_mandir}/man1/latexrevise.1*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n latexdiff

%build

%install
mkdir -p %{buildroot}/%{_bindir} \
	%{buildroot}/%{_mandir}/man1
cp -p latexdiff %{buildroot}/%{_bindir}/latexdiff
cp -p latexdiff-fast %{buildroot}/%{_bindir}/latexdiff-fast
cp -p latexdiff-so %{buildroot}/%{_bindir}/latexdiff-so
cp -p latexdiff-vc %{buildroot}/%{_bindir}/latexdiff-vc
cp -p latexrevise %{buildroot}/%{_bindir}/latexrevise
cp -p *.1 %{buildroot}/%{_mandir}/man1
chmod 644 %{buildroot}/%{_mandir}/man1/*

