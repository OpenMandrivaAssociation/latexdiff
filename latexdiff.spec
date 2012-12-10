Summary: Determine and mark up significant differences between latex files
Name: latexdiff
Version: 0.5
Release: %mkrel 4
URL: http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=latexdiff
Source: http://tug.ctan.org/cgi-bin/getFile.py?fn=/systems/win32/miktex/tm/packages/latexdiff.tar.bz2
License: GPLv2
Group: Text tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} <= 200900
Requires: tetex-latex
%else
#Is this working?
Requires: tex(latex)
%endif
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

%prep
%setup -q -c

%build
chmod 644 texmf/source/latexdiff/example/*.tex

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir} \
	%{buildroot}/%{_mandir}/man1
cp -p texmf/scripts/latexdiff/perl/latexdiff-fast.pl %{buildroot}/%{_bindir}/latexdiff
cp -p texmf/scripts/latexdiff/perl/latexdiff-vc.pl %{buildroot}/%{_bindir}/latexdiff-vc
cp -p texmf/scripts/latexdiff/perl/latexrevise.pl %{buildroot}/%{_bindir}/latexrevise
cp -p texmf/source/latexdiff/latex{diff,diff-vc,revise}.1 %{buildroot}/%{_mandir}/man1
chmod 644 %{buildroot}/%{_mandir}/man1/*
chmod 644 texmf/doc/support/latexdiff/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc texmf/doc/support/latexdiff/* texmf/source/latexdiff/example/*.tex
%attr(755,root,root) %{_bindir}/latexdiff
%attr(755,root,root) %{_bindir}/latexdiff-vc
%attr(755,root,root) %{_bindir}/latexrevise
%attr(644,root,root) %{_mandir}/man1/latexdiff.1*
%attr(644,root,root) %{_mandir}/man1/latexdiff-vc.1*
%attr(644,root,root) %{_mandir}/man1/latexrevise.1*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-4mdv2011.0
+ Revision: 620050
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2010.0
+ Revision: 438178
- rebuild

* Fri Feb 06 2009 Giuseppe Ghibò <ghibo@mandriva.com> 0.5-2mdv2009.1
+ Revision: 338177
- Fix permissions (rpmlint-aware).
- Add examples to docs.
- Fix Requires for older releases.

* Sun Jan 11 2009 Jérôme Soyer <saispo@mandriva.org> 0.5-1mdv2009.1
+ Revision: 328365
- import latexdiff


