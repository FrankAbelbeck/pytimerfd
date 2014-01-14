#!/usr/bin/env python
r"""This file is part of pytimerfd (a Python wrapper module for timerfd.h)
Copyright (C) 2013 Frank Abelbeck <frank.abelbeck@googlemail.com>

    pytimerfd is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pytimerfd is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with pytimerfd.  If not, see <http://www.gnu.org/licenses/>."""

from distutils.core import setup, Extension

timerfdmodule = Extension("timerfd", sources = ["timerfd.c"])

longdescription = """"These system calls create and operate on a timer that delivers timer expiration
notifications via a file descriptor. They provide an alternative to the use of
setitimer() or timer_create(), with the advantage that the file descriptor may
be monitored by select(), poll(), and epoll()." [source: manpage timerfg_create]"""

setup(
	name = "pytimerfd",
	version = "1.2",
	description = "Python bindings for the Linux timerfd_* syscalls",
	long_description = longdescription,
	author = "Frank Abelbeck",
	author_email = "frank.abelbeck@googlemail.com",
	url = "https://abelbeck.wordpress.com",
	license = "LGPL",
	platforms = "Linux",
	ext_modules = [timerfdmodule]
)
