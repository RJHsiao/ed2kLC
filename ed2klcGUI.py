#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the GUI part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/12/17
# Version: 1.0

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
		wx.Frame.__init__(self, parent, id, title = u'ed2k Link Converter', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.WANTS_CHARS)
		self.Icon = ed2klcIcon.getIconIcon()
		self.SetIcon(self.Icon)

		globalPanel = wx.Panel(self)
		globalSizer = wx.BoxSizer()

		## Main area, contain input text box, option radio boxs and result (output) Text Box
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		## The area that contain input text box 
		inputSizer = wx.StaticBoxSizer(wx.StaticBox(globalPanel, label = u'Input Links'))
		self.inputText = wx.TextCtrl(globalPanel, size = (350, 150), style = wx.TE_MULTILINE | wx.HSCROLL)
		inputSizer.Add(self.inputText, 0, wx.ALL, 5)
		mainSizer.AddSizer(inputSizer, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain option radio boxs
		optionSizer = wx.StaticBoxSizer(wx.StaticBox(globalPanel, label = u'Options'))
		self.tagRB = wx.RadioBox(globalPanel, label = u'Tag Type', choices = [u'No Tag', u'HTML', u'BBcode'])
		optionSizer.Add(self.tagRB, 0, wx.ALL, 5)
		self.isUTF8URL_RB = wx.RadioBox(globalPanel, label = u'with UTF-8 encode?', choices = [u'Yes',u'No'])
		optionSizer.Add(self.isUTF8URL_RB, 0, wx.ALL, 5)
		mainSizer.AddSizer(optionSizer, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain result (output) text box
		resultSizer = wx.StaticBoxSizer(wx.StaticBox(globalPanel, label = u'Converted Links'))
		self.resultText = wx.TextCtrl(globalPanel, size = (350, 150), style = wx.TE_MULTILINE | wx.HSCROLL)
		resultSizer.Add(self.resultText, 0, wx.ALL, 5)
		mainSizer.AddSizer(resultSizer, 0, wx.EXPAND | wx.ALL, 5)

		globalSizer.AddSizer(mainSizer, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain all buttons
		buttonSizer = wx.BoxSizer(wx.VERTICAL)

		## The Convert Button
		convertBtn = wx.Button(globalPanel, label = u'Convert')
		buttonSizer.Add(convertBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnConvert, id = convertBtn.GetId())

		## The Clean Button
		clearBtn = wx.Button(globalPanel, wx.ID_CLEAR)
		buttonSizer.Add(clearBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnClear, id = wx.ID_CLEAR)

		## The About Button
		aboutBtn = wx.Button(globalPanel, wx.ID_ABOUT)
		buttonSizer.Add(aboutBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnAbout, id = wx.ID_ABOUT)

		## The Exit Button
		exitBtn = wx.Button(globalPanel, wx.ID_EXIT)
		buttonSizer.Add(exitBtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnExit, id = wx.ID_EXIT)

		globalSizer.AddSizer(buttonSizer, 0, wx.EXPAND | wx.ALL, 5)

		globalPanel.SetSizer(globalSizer)
		globalSizer.SetSizeHints(self)
		self.inputText.SetFocus()
		globalPanel.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)
		self.inputText.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)
		self.resultText.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)
		self.Centre()

	def OnConvert(self, event):
		""" Convert ed2k link """
		self.resultText.Clear()
		hasConvert = False
		hasError = False
		errorLines = []
		for i in range(self.inputText.GetNumberOfLines()):
			result = ed2kConvert.ConvertLink(
				inputLink = self.inputText.GetLineText(i),
				desType = self.tagRB.GetSelection(),
				isUTF8URL = not bool(self.isUTF8URL_RB.GetSelection()))
			if result == None:
				errorLines.append(i+1)
				hasError = True
				self.resultText.write('\n')
			elif result == '':
				if hasConvert == True:
					self.resultText.write('\n')
			else:
				self.resultText.write(result)
				hasConvert = True
		self.inputText.SetFocus()
		if hasError == True:
			dlg = wx.MessageDialog(self, message = u'Found non-regular ed2k link(s)!\nLine: ' + str(errorLines)[1:-1], caption = u'Oops!', style = wx.OK)
			dlg.ShowModal()
			dlg.Destroy()
		if hasConvert == True:
			while self.resultText.GetValue()[-2:] == '\n\n':
				self.resultText.SetValue(self.resultText.GetValue()[:-1])
			dlg = wx.MessageDialog(self, message = u'Convert Finished', caption = u'ed2k Link Converter', style = wx.OK)
			dlg.ShowModal()
			dlg.Destroy()
			self.resultText.SetFocus()
			self.resultText.SelectAll()
			self.resultText.Copy()

	def OnClear(self, event):
		""" Clean up input & result text area """
		self.inputText.Clear()
		self.resultText.Clear()
		self.inputText.SetFocus()

	def OnAbout(self, event):
		""" Print Adout Dialog """
		aboutdlginfo = wx.AboutDialogInfo()
		aboutdlginfo.AddDeveloper(u'Wei-Jie Hsiao (a.k.a. RJ)')
		aboutdlginfo.SetCopyright(u'Copyright @ 2010 Wei-Jie Hsiao')
		aboutdlginfo.SetIcon(self.Icon)
		aboutdlginfo.SetLicence(
			u"ed2k Link Converter - a ed2k tag and link-format converter.\n\n" +
			u"This program is free software: you can redistribute it and/or\n" +
			u"modify it under the terms of the GNU General Public License\n" +
			u"as published by the Free Software Foundation, either\n" +
			u"version 3 of the License, or (at your option) any later version.\n\n" +
			u"This program is distributed in the hope that it will be useful,\n" +
			u"but WITHOUT ANY WARRANTY; without even the implied\n" +
			u"warranty of MERCHANTABILITY or FITNESS FOR A\n" +
			u"PARTICULAR PURPOSE. See the GNU General Public License\n" +
			u"for more details.\n\n" +
			u"You should have received a copy of the GNU General Public\n" +
			u"License along with this program. If not, see\n" +
			u"<http://www.gnu.org/licenses/>.")
		aboutdlginfo.SetName(u'ed2k Link Converter')
		aboutdlginfo.SetVersion(u'v1.0')
		aboutdlginfo.SetWebSite(u'http://github.com/RJking/ed2kLC')
		wx.AboutBox(aboutdlginfo)

	def OnKeyPress(self, event):
		keycode = event.GetKeyCode()
		if event.ShiftDown() and keycode in [wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER]: #Press Shift+Enter
			self.OnConvert(event)
		elif event.CmdDown() and keycode == 81: #Press Ctrl+Q
			self.Close()
		else:
			event.Skip()

	def OnExit(self, event):
		self.Close(True)

def RunGUI():
	app = wx.App()
	GUIWindow(None, wx.ID_ANY).Show(True)
	app.MainLoop()
