# revision 16549
# category Package
# catalog-ctan /macros/latex/contrib/nomentbl
# catalog-date 2007-01-12 00:17:35 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-nomentbl
Version:	0.4
Release:	8
Summary:	Nomenclature typeset in a longtable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nomentbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomentbl.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 754355
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 719127
- texlive-nomentbl
- texlive-nomentbl
- texlive-nomentbl
- texlive-nomentbl

