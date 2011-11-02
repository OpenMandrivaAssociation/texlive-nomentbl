Name:		texlive-nomentbl
Version:	0.4
Release:	1
Summary:	Nomenclature typeset in a longtable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nomentbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Nomentbl typeset nomenclatures in a longtable instead of the
makeindex style of nomencl. A nomenclature entry may have three
arguments: Symbol, description and physical unit.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
