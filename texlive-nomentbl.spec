%global tl_name nomentbl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Nomenclature typeset in a longtable
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nomentbl
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Nomentbl typeset nomenclatures in a longtable instead of the makeindex
style of nomencl. A nomenclature entry may have three arguments: Symbol,
description and physical unit.

