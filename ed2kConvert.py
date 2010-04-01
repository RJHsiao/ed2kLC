#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the Convert part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/03/18
# Version: 0.1

### Program Start
import codecs
import urllib
import re

filename = ''

def ConvertLink(srclink, destype = u'', utf8url = True):
	#
	if srclink == u'':
		return u''
	filename = urllib.unquote_plus(srclink.split(u'|')[2])
	f = codecs.open(u'test.txt','w','utf_8')
	f.write(filename + '\n')
	f.close()
	return unicode(u'<a href="' + srclink + u'">' + filename + u'</a>')
