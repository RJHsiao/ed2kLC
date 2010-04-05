#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the Convert part
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
import urllib
import re

## Defind constant
NOTAG = 0
TAG_HTML = 1
TAG_BBCODE = 2

ed2kQuoteSafe = ":,/|=!@#$%^&_-+'`~[](){}"
ed2kQuoteSafe_BBbbcode = ":,/|=!@#$%^&_-+'`~(){}"

## the ed2k file link format regex
ed2kFileLinkRegex = re.compile(\
	'(ed2k://\|file\|(.+?)\|\d+\|[a-fA-F0-9]{32}\|' + \
	'(((p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?(h=\w{32}\|)?(s=http://[\w\.-_&%/]+\|)*)|' + \
	'((p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?(s=http://[\w\.-_&%/]+\|)*(h=\w{32}\|)?)|' + \
	'((h=\w{32}\|)?(p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?(s=http://[\w\.-_&%/]+\|)*)|' + \
	'((h=\w{32}\|)?(s=http://[\w\.-_&%/]+\|)*(p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?)|' + \
	'((s=http://[\w\.-_&%/]+\|)*(p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?(h=\w{32}\|)?)|' + \
	'((s=http://[\w\.-_&%/]+\|)*(h=\w{32}\|)?(p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?))' + \
	'/(\|sources,[\w\.-_]+:\d{1,5}\|/)?)')

ed2kLinkTemplate = ['{0}\n','<a href="{0}">{1}</a>\n','[url={0}]{1}[/url]\n']

def ConvertLink(inputLink, desType = NOTAG, isUTF8URL = True):
	"""
	ConvertLink(inputLink, desType = ed2kConvert.NOTAG, utf8url = True)
	"""
	if inputLink == '':
		return '\n'
	detectLink = ed2kFileLinkRegex.findall(inputLink)
	if detectLink == []:
		return None
	returnStr = ''
	for ed2kLink in detectLink:
		if isUTF8URL is True:
			srcLink = urllib.quote(ed2kLink[0], ed2kQuoteSafe)
		else:
			srcLink = urllib.unquote(ed2kLink[0].encode('utf_8'))
		if desType is TAG_BBCODE:
			pass # In this case, we have to convert '[' & ']' to utf8 format. If not 
			srcLink = srcLink.replace('[','%5B').replace(']','%5D')
		fileName = urllib.unquote(ed2kLink[1].encode('utf_8'))
		returnStr += ed2kLinkTemplate[desType].format(srcLink, fileName).decode('utf_8')
	return returnStr
