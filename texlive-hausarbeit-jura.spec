# revision 25356
# category Package
# catalog-ctan /macros/latex/contrib/hausarbeit-jura
# catalog-date 2012-02-10 13:14:08 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-hausarbeit-jura
Version:	1.0
Release:	1
Summary:	Class for writing "juristiche Hausarbeiten" at German Universities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hausarbeit-jura
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class was developed to write legal essays ("juristische
Hausarbeit") at German Universities. It is based on jurabook
and jurabib and makes it easy for LaTeX beginners to get a
correct and nicely formatted paper.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hausarbeit-jura/hausarbeit-jura.cls
%doc %{_texmfdistdir}/doc/latex/hausarbeit-jura/README
%doc %{_texmfdistdir}/doc/latex/hausarbeit-jura/README.
%doc %{_texmfdistdir}/doc/latex/hausarbeit-jura/hausarbeit-demo.bib
%doc %{_texmfdistdir}/doc/latex/hausarbeit-jura/hausarbeit-demo.tex
#- source
%doc %{_texmfdistdir}/source/latex/hausarbeit-jura/hausarbeit-jura.dtx
%doc %{_texmfdistdir}/source/latex/hausarbeit-jura/hausarbeit-jura.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 779749
- Import texlive-hausarbeit-jura
- Import texlive-hausarbeit-jura

