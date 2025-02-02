Name:		texlive-relenc
Version:	22050
Release:	2
Summary:	A "relaxed" font encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/relenc
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relenc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relenc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX package providing a relaxed font encoding to make
available to a font designer more slots for insertion of
ligatures and accented characters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/relenc/zcmr8d.tfm
%{_texmfdistdir}/fonts/tfm/public/relenc/zcmra.tfm
%{_texmfdistdir}/fonts/vf/public/relenc/zcmr8d.vf
%{_texmfdistdir}/fonts/vf/public/relenc/zcmra.vf
%{_texmfdistdir}/tex/latex/relenc/2sidedoc.sty
%{_texmfdistdir}/tex/latex/relenc/ecsubzcm.sty
%{_texmfdistdir}/tex/latex/relenc/relenc.sty
%{_texmfdistdir}/tex/latex/relenc/t1renc.def
%{_texmfdistdir}/tex/latex/relenc/t1rzcm.fd
%doc %{_texmfdistdir}/doc/latex/relenc/README
%doc %{_texmfdistdir}/doc/latex/relenc/reldemo.tex
%doc %{_texmfdistdir}/doc/latex/relenc/relenc.tex
%doc %{_texmfdistdir}/doc/latex/relenc/zcmr8d.vf2
%doc %{_texmfdistdir}/doc/latex/relenc/zcmr8d.vf3
%doc %{_texmfdistdir}/doc/latex/relenc/zcmra.vf2
%doc %{_texmfdistdir}/doc/latex/relenc/zcmra.vf3
#- source
%doc %{_texmfdistdir}/source/latex/relenc/relenc.dtx
%doc %{_texmfdistdir}/source/latex/relenc/relenc.ins
%doc %{_texmfdistdir}/source/latex/relenc/t1renc.dtx
%doc %{_texmfdistdir}/source/latex/relenc/t1rzcm.fdd

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
