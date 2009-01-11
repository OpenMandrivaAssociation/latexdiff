Summary: Determine and mark up significant differences between latex files
Name: latexdiff
Version: 0.5
Release: %mkrel 1
URL: http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=latexdiff
Source: http://tug.ctan.org/cgi-bin/getFile.py?fn=/systems/win32/miktex/tm/packages/latexdiff.tar.bz2
License: GPLv2
Group: Text tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: tex(latex)
BuildArch: noarch

%description
Latexdiff is a Perl script for visual mark up and revision of significant
differences between two latex files.  Various options are available for visual
markup using standard latex packages such as color.  Changes not directly
affecting visible text, for example in formatting commands, are still marked in
the latex source.  A rudimentary revision facility is provided by another
Perl script, latexrevise, which accepts or rejects all changes.  Manual editing
of the difference file can be used to override this default behaviour and
accept or reject selected changes only.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1
cp -p texmf/scripts/latexdiff/perl/latexdiff-fast.pl %{buildroot}/%{_bindir}/latexdiff
cp -p texmf/scripts/latexdiff/perl/latexdiff-vc.pl %{buildroot}/%{_bindir}/latexdiff-vc
cp -p texmf/scripts/latexdiff/perl/latexrevise.pl %{buildroot}/%{_bindir}/latexrevise
cp -p texmf/source/latexdiff/latex{diff,diff-vc,revise}.1 %{buildroot}/%{_mandir}/man1
chmod a-x %{buildroot}/%{_mandir}/man1/*
chmod a-x texmf/doc/support/latexdiff/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc texmf/doc/support/latexdiff/*
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise
%{_mandir}/man1/latexdiff.1*
%{_mandir}/man1/latexdiff-vc.1*
%{_mandir}/man1/latexrevise.1*
