# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=5
PYTHON_COMPAT=( python{2_7,3_2} )

inherit distutils-r1 linux-info

DESCRIPTION="Python bindings for the Linux timerfd_* syscalls"
HOMEPAGE="http://pypi.python.org/pypi/pytimerfd http://abelbeck.wordpress.com/"
SRC_URI="mirror://pypi/${PN:0:1}/${PN}/${P}.tar.gz"

LICENSE="LGPL"
SLOT="0"
KEYWORDS="~amd64"
IUSE=""

DEPEND=""
RDEPEND=""

CONFIG_CHECK="TIMERFD"
ERROR_TIMERFD="${PN} requires support for timerfd() system calls (TIMERFD), being enabled in 'General setup -> Configure standard kernel features (expert users)'."

pkg_setup() {
	linux-info_pkg_setup
}

python_install_all() {
	local DOCS=( COPYING README )
	distutils-r1_python_install_all
}
