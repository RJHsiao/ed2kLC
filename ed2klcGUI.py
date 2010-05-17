#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the GUI part
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
import wx
import ed2kConvert
import ed2klcIcon

class GUIWindow(wx.Frame):
	"""The GUI Window"""
	
	def __init__(self, parent, id):
		## These variable are define for support multi-language in the future
		self.title = u'ed2k Link Converter'
		self.inputLabel = u'Input Links'
		self.optionLabel = u'Options'
		self.tagLabel = u'Tag Type'
		self.tagChoices = [u'No Tag', u'HTML', u'BBcode']
		self.isUTF8URL_Label = u'UTF-8 url format?'
		self.isUTF8URL_Choices = [u'Yes',u'No']
		self.resultLabel = u'Converted Links'
		self.cleanBtnLabel = u'Clean'
		self.convertBtnLabel = u'Convert'
		self.aboutBtnLabel = u'About'
		self.exitBtuLabel = u'Exit'
		self.langChoices = [u'English (en)',u'正體中文 (zh-TW)']
		self.linkNotMatchMsg = u'Line {0} is not a regular ed2k file link!'
		self.noticeDlgCaption = u'Oops!'
		self.convertFinMsg = u'Convert Finished'

		POS = wx.DefaultPosition
		SIZE = (500,550)
		Style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
		wx.Frame.__init__(self, parent, id, title = self.title, pos = POS, size = SIZE, style = Style)
		self.Icon = ed2klcIcon.getIconIcon()
		self.SetIcon(self.Icon)

		self.globalPanel = wx.Panel(self,-1)
		self.globalBox = wx.BoxSizer(wx.HORIZONTAL)

		## Main area, contain input text box, option radio boxs and result (output) Text Box
		mainPanel = wx.Panel(self.globalPanel,-1)
		mainBox = wx.BoxSizer(wx.VERTICAL)

		## The area that contain input text box 
		inputPanel = wx.Panel(mainPanel, -1)
		inputBox = wx.StaticBoxSizer(wx.StaticBox(inputPanel, -1, self.inputLabel), orient = wx.VERTICAL)
		self.inputText = wx.TextCtrl(inputPanel, -1, size = (350, 150), style = wx.TE_MULTILINE | wx.HSCROLL)
		inputBox.Add(self.inputText, 0, wx.ALL, 5)
		inputPanel.SetSizer(inputBox)
		mainBox.Add(inputPanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain option radio boxs
		optionPanel = wx.Panel(mainPanel, -1)
		optionBox = wx.StaticBoxSizer(wx.StaticBox(optionPanel, -1, self.optionLabel), orient = wx.HORIZONTAL)
		self.tagRB = wx.RadioBox(optionPanel, -1, label = self.tagLabel, choices = self.tagChoices)
		optionBox.Add(self.tagRB, 0, wx.ALL, 5)
		self.isUTF8URL_RB = wx.RadioBox(optionPanel, -1, label = self.isUTF8URL_Label, choices = self.isUTF8URL_Choices)
		optionBox.Add(self.isUTF8URL_RB, 0, wx.ALL, 5)
		optionPanel.SetSizer(optionBox)
		mainBox.Add(optionPanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain result (output) text box
		resultPanel = wx.Panel(mainPanel, -1)
		resultBox = wx.StaticBoxSizer(wx.StaticBox(resultPanel, -1, self.resultLabel), orient = wx.VERTICAL)
		self.resultText = wx.TextCtrl(resultPanel, -1, size = (350, 150), style = wx.TE_MULTILINE)
		resultBox.Add(self.resultText, 0, wx.ALL, 5)
		resultPanel.SetSizer(resultBox)
		mainBox.Add(resultPanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain languade select combo box <future work>
		langPanel = wx.Panel(mainPanel, -1)
		langBox = wx.BoxSizer(wx.HORIZONTAL)
		langLabel = wx.StaticText(langPanel, -1, u'Language:')
		self.langCB = wx.ComboBox(langPanel, -1, size = (150, -1), choices = self.langChoices, style = wx.CB_READONLY)
		self.langCB.SetSelection(0)
		self.Bind(wx.EVT_TEXT, self.OnChangeLang, id = self.langCB.GetId())
		langBox.Add(langLabel, 0, wx.ALL, 5)
		langBox.Add(self.langCB, 0, wx.ALL, 5)
		langPanel.SetSizer(langBox)
		mainBox.Add(langPanel, 0, wx.EXPAND | wx.ALL, 5)

		mainPanel.SetSizer(mainBox)
		self.globalBox.Add(mainPanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain all buttons
		buttonPanel = wx.Panel(self.globalPanel, -1)
		buttonBox = wx.BoxSizer(wx.VERTICAL)
		BTNSIZE = (50, 30)

		## The Convert Button
		convertBtn = wx.Button(buttonPanel, -1, self.convertBtnLabel,)
		buttonBox.Add(convertBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnConvert, id = convertBtn.GetId())

		## The Clean Button
		cleanBtn = wx.Button(buttonPanel, -1, self.cleanBtnLabel,)
		buttonBox.Add(cleanBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnClean, id = cleanBtn.GetId())

		## The About Button
		aboutBtn = wx.Button(buttonPanel, -1, self.aboutBtnLabel, BTNSIZE)
		buttonBox.Add(aboutBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnAbout, id = aboutBtn.GetId())

		## The Exit Button
		exitBtn = wx.Button(buttonPanel, -1, self.exitBtuLabel, BTNSIZE)
		buttonBox.Add(exitBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnExit, id = exitBtn.GetId())

		buttonPanel.SetSizer(buttonBox)
		self.globalBox.Add(buttonPanel, 0, wx.EXPAND | wx.ALL, 5)

		self.globalPanel.SetSizer(self.globalBox)
		#self.SetSizer(self.globalBox)
		self.globalBox.SetSizeHints(self)
		self.Centre()

	def OnConvert(self, e):
		""" Convert ed2k link """
		self.resultText.Clear()
		for i in range(self.inputText.GetNumberOfLines()):
			result = ed2kConvert.ConvertLink(\
				inputLink = self.inputText.GetLineText(i),\
				desType = self.tagRB.GetSelection(),\
				isUTF8URL = not bool(self.isUTF8URL_RB.GetSelection()))
			if result == None:
				dlg = wx.MessageDialog(self, message = self.linkNotMatchMsg.format(i + 1), caption = self.noticeDlgCaption, style = wx.OK)
				dlg.ShowModal()
				dlg.Destroy()
				return False
			else:
				self.resultText.write(result)
		dlg = wx.MessageDialog(self, message = self.convertFinMsg, caption = self.title, style = wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnChangeLang(self, e):
		""" Change GUI Language """
		dlg = wx.MessageDialog(self, message=u'This feature is not finished yet...', caption= self.noticeDlgCaption, style = wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
		self.langCB.SetSelection(0)

	def OnClean(self, e):
		""" Clean up input & result text area """
		self.inputText.Clear()
		self.resultText.Clear()

	def OnAbout(self, e):
		""" Print Adout Dialog """
		aboutdlginfo = wx.AboutDialogInfo()
		aboutdlginfo.AddDeveloper(u'Wei-Jie Hsiao (a.k.a. RJ)')
		aboutdlginfo.SetCopyright(u'Copyright @ 2010 Wei-Jie Hsiao')
		aboutdlginfo.SetIcon(self.Icon)
		aboutdlginfo.SetLicence(u"ed2k Link Converter - a ed2k tag and link-format converter.\n\n" + \
								u"This program is free software: you can redistribute it and/or\n" + \
								u"modify it under the terms of the GNU General Public License\n" + \
								u"as published by the Free Software Foundation, either\n" + \
								u"version 3 of the License, or (at your option) any later version.\n\n" + \
								u"This program is distributed in the hope that it will be useful,\n" + \
								u"but WITHOUT ANY WARRANTY; without even the implied\n" + \
								u"warranty of MERCHANTABILITY or FITNESS FOR A\n" + \
								u"PARTICULAR PURPOSE. See the GNU General Public License\n" + \
								u"for more details.\n\n" + \
								u"You should have received a copy of the GNU General Public\n" + \
								u"License along with this program. If not, see\n" + \
								u"<http://www.gnu.org/licenses/>.")
		aboutdlginfo.SetName(u'ed2k Link Converter')
		aboutdlginfo.SetVersion(u'v0.1.1')
		aboutdlginfo.SetWebSite(u'http://github.com/RJking/ed2kLC')
		wx.AboutBox(aboutdlginfo)

	def OnExit(self, e):
		self.Close(True)

def RunGUI():
	app = wx.App()
	GUIWindow(None, wx.ID_ANY).Show(True)
	app.MainLoop()
