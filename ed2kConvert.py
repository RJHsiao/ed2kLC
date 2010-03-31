#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the Convert part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/03/18
# Version: 0.1

### Program Start
import urllib
import re

def ConvertLink(srclink, destype = '', utf8url = True):
	#
	if srclink == '':
		return ''
	filename = srclink.split('|')[2]
	return unicode('<a href="' + srclink + '">' + urllib.unquote_plus(filename) + '</a>')
