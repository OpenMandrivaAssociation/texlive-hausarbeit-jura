%global tl_name hausarbeit-jura
%global tl_revision 56070

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.0
Release:	%{tl_revision}.1
Summary:	Class for writing juristische Hausarbeiten at German Universities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hausarbeit-jura
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hausarbeit-jura.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class was developed for use by students writing legal essays
("juristische Hausarbeit") at German Universities. It is based on
jurabook and jurabib and makes it easy for LaTeX beginners to get a
correct and nicely formatted paper.

