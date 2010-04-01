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
	if srclink == '':
		return ''
	filename = urllib.unquote_plus(srclink.encode('utf_8').split('|')[2]).decode('utf8')
	return '<a href="' + srclink + '">' + filename + '</a>'
	