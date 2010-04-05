#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Program Name: ed2k Link Converter
# THis is a program that can Converse edk2 link like:
#	1.UTF-8 <-> MBCS / Unicode charactor you can read
#	2.add / remove the html / BBcode tag
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
import ed2klcGUI

def main():
	ed2klcGUI.RunGUI()

if __name__ == "__main__":
	main()