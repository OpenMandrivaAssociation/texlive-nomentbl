Name:		texlive-nomentbl
Version:	16549
Release:	2
Summary:	Nomenclature typeset in a longtable
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nomentbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Nomentbl typeset nomenclatures in a longtable instead of the
makeindex style of nomencl. A nomenclature entry may have three
arguments: Symbol, description and physical unit.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/nomentbl/nomentbl.ist
%{_texmfdistdir}/tex/latex/nomentbl/nomentbl.sty
%doc %{_texmfdistdir}/doc/latex/nomentbl/README
%doc %{_texmfdistdir}/doc/latex/nomentbl/example.pdf
%doc %{_texmfdistdir}/doc/latex/nomentbl/example.tex
%doc %{_texmfdistdir}/doc/latex/nomentbl/nomentbl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nomentbl/nomentbl.dtx
%doc %{_texmfdistdir}/source/latex/nomentbl/nomentbl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
