Name:		texlive-old-arrows
Version:	42872
Release:	2
Summary:	Computer Modern old-style arrows with smaller arrowheads
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/old-arrows
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/old-arrows.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/old-arrows.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides Computer Modern old-style arrows with
smaller arrowheads, associated with the usual LaTeX commands.
It can be used in documents that contain other amssymb arrow
characters that also have small arrowheads. It is also possible
to use the usual new-style Computer Modern arrows together with
the old-style ones.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/old-arrows
%{_texmfdistdir}/fonts/type1/public/old-arrows
%{_texmfdistdir}/fonts/tfm/public/old-arrows
%{_texmfdistdir}/fonts/map/dvips/old-arrows
%{_texmfdistdir}/fonts/enc/dvips/old-arrows
%{_texmfdistdir}/fonts/afm/public/old-arrows
%doc %{_texmfdistdir}/doc/fonts/old-arrows

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
