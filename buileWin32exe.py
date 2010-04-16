#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the Windoes execute file builder part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/04/05
# Version: 0.1

##########################################################################
#                                 LICENSE                                #
##########################################################################
# This file is part of ed2k Link Converter.                              #
#                                                                        #
# ed2k Link Converter is free software: you can redistribute it          #
# and/or modify it under the terms of the GNU General Public License     #
# as published by the Free Software Foundation, either                   #
# version 3 of the License, or (at your option) any later version.       #
#                                                                        #
# ed2k Link Converter is distributed in the hope that it will be useful, #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with ed2k Link Converter.  If not, see                           #
# <http://www.gnu.org/licenses/>.                                        #
##########################################################################

### Program Start
from distutils.core import setup
import py2exe

includes = ['encodings', 'encodings.*']

setup(name='ed2kLC',
		description = 'ed2k Link Converter',
		version = '0.1.1',
		data_files=[('', ['ed2klc.ico'])],
		windows = [{'script' : 'ed2klc.py', 'icon_resources' : [(1, 'ed2klc.ico')]}],
		zipfile = None,
		options = {'py2exe':{'compressed' : 2,
								'optimize' : 2,
								'bundle_files' : 1,
								'ascii' : False,
								'includes' : includes,}})
