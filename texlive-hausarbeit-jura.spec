Name:		texlive-hausarbeit-jura
Version:	56070
Release:	2
Summary:	Class for writing "juristiche Hausarbeiten" at German Universities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hausarbeit-jura
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class was developed for use by students writing legal
essays ("juristische Hausarbeit") at German Universities. It is
based on jurabook and jurabib and makes it easy for LaTeX
beginners to get a correct and nicely formatted paper.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hausarbeit-jura
%doc %{_texmfdistdir}/doc/latex/hausarbeit-jura
#- source
%doc %{_texmfdistdir}/source/latex/hausarbeit-jura

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
