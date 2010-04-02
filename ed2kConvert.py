#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the Convert part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/03/18
# Version: 0.1

### Program Start
import urllib
import re

ed2kFileRule = re.compile('(ed2k://\|file\|(.+)\|\d+\|[a-fA-F0-9]{32}\|(p=[a-fA-F0-9]{32}(:[a-fA-F0-9]{32})*\|)?(h=\w{32}\|)?(s=http://[\w\.-_&%/]+\|)*/(\|sources,[\w\.-_]+:\d{1,5}\|/)?)')

def ConvertLink(srclink, destype = '', utf8url = True):
	if srclink == '':
		return ''
	checklink = ed2kFileRule.findall(srclink)
	if checklink == []:
		return None
	else:
		#filename = urllib.unquote_plus(srclink.encode('utf_8').split('|')[2]).decode('utf8')
		filename = urllib.unquote_plus(checklink[0][1].encode('utf_8')).decode('utf8')
		return '<a href="' + srclink + '">' + filename + '</a>'
