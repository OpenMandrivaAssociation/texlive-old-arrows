%global tl_name old-arrows
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Computer Modern old-style arrows with smaller arrowheads
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/old-arrows
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/old-arrows.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/old-arrows.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides Computer Modern old-style arrows with smaller
arrowheads, associated with the usual LaTeX commands. It can be used in
documents that contain other amssymb arrow characters that also have
small arrowheads. It is also possible to use the usual new-style
Computer Modern arrows together with the old-style ones.

