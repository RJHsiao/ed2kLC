#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the GUI part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/03/18
# Version: 0.1

### Program Start
import wx
import ed2kConvert

class GUIWindow(wx.Frame):
	"""The GUI Window"""
	def __init__(self, parent, id):
		## These variable are define for support multi-language in the future
		Title = u'ed2k Link Converter'
		inputlabel = u'Input Links'
		optionlabel = u'Options'
		taglabel = u'Tag Type'
		tagchoices = [u'HTML',u'BBcode',u'No Tag']
		formatlabel = u'UTF-8 url format' + u'?'
		formatchoices = [u'Yes',u'No']
		resultlabel = u'Result Links'
		convertbtnlabel = u'Convert'
		aboutbtnlabel = u'About'
		exitbtulabel = u'Exit'
		langchoices = [u'English (en)']#,u'正體中文 (zh-TW)'] 

		Pos = wx.DefaultPosition
		Size = (500,550)
		Style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
		#self.Icon = wx.Icon(u'icon', wx.BITMAP_TYPE_ICO)
		#self.Icon.CopyFromBitmap(self,wx.Image(u'ed2klc.ico', wx.BITMAP_TYPE_ICO).ConvertToBitmap())
		wx.Frame.__init__(self, parent, id, title = Title, pos = Pos, size = Size, style = Style)

		gobalpanel = wx.Panel(self, -1)
		gobalbox = wx.BoxSizer(wx.HORIZONTAL)

		## Main area, contain input text box, option radio boxs and result (output) Text Box
		mainpanel = wx.Panel(gobalpanel,-1)
		mainbox = wx.BoxSizer(wx.VERTICAL)

		## The area that contain input text box 
		inputpanel = wx.Panel(mainpanel, -1)
		inputbox = wx.StaticBoxSizer(wx.StaticBox(inputpanel, -1, inputlabel), orient = wx.VERTICAL)
		self.inputtext = wx.TextCtrl(inputpanel, -1, size = (350, 150), style = wx.TE_MULTILINE | wx.HSCROLL)
		inputbox.Add(self.inputtext, 0, wx.ALL, 5)
		inputpanel.SetSizer(inputbox)
		mainbox.Add(inputpanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain option radio boxs
		optionpanel = wx.Panel(mainpanel, -1)
		optionbox = wx.StaticBoxSizer(wx.StaticBox(optionpanel, -1, optionlabel), orient = wx.HORIZONTAL)
		self.tagrb = wx.RadioBox(optionpanel, -1, label = taglabel, choices = tagchoices)
		optionbox.Add(self.tagrb, 0, wx.ALL, 5)
		self.formatrb = wx.RadioBox(optionpanel, -1, label = formatlabel, choices = formatchoices)
		optionbox.Add(self.formatrb, 0, wx.ALL, 5)
		optionpanel.SetSizer(optionbox)
		mainbox.Add(optionpanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain result (output) text box
		resultpanel = wx.Panel(mainpanel, -1)
		resultbox = wx.StaticBoxSizer(wx.StaticBox(resultpanel, -1, resultlabel), orient = wx.VERTICAL)
		self.resulttext = wx.TextCtrl(resultpanel, -1, size = (350, 150), style = wx.TE_MULTILINE)
		resultbox.Add(self.resulttext, 0, wx.ALL, 5)
		resultpanel.SetSizer(resultbox)
		mainbox.Add(resultpanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain languade select combo box <future work>
		langpanel = wx.Panel(mainpanel, -1)
		langbox = wx.BoxSizer(wx.HORIZONTAL)
		langlabel = wx.StaticText(langpanel, -1, u'Language:')
		langcb = wx.ComboBox(langpanel, -1, size = (150, -1), choices = langchoices)
		langcb.SetSelection(0)
		langbox.Add(langlabel, 0, wx.ALL, 5)
		langbox.Add(langcb, 0, wx.ALL, 5)
		langpanel.SetSizer(langbox)
		mainbox.Add(langpanel, 0, wx.EXPAND | wx.ALL, 5)

		mainpanel.SetSizer(mainbox)
		gobalbox.Add(mainpanel, 0, wx.EXPAND | wx.ALL, 5)

		## The area that contain all buttons
		buttonpanel = wx.Panel(gobalpanel, -1)
		buttonbox = wx.BoxSizer(wx.VERTICAL)
		btnsize = (50, 30)

		## The Convert Button
		convertbtn = wx.Button(buttonpanel, -1, convertbtnlabel,)
		buttonbox.Add(convertbtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnConvert, id = convertbtn.GetId())

		## The About Button
		aboutbtn = wx.Button(buttonpanel, -1, aboutbtnlabel, btnsize)
		buttonbox.Add(aboutbtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnAbout, id = aboutbtn.GetId())

		## The Exit Button
		exitbtn = wx.Button(buttonpanel, -1, exitbtulabel, btnsize)
		buttonbox.Add(exitbtn, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.OnExit, id = exitbtn.GetId())

		buttonpanel.SetSizer(buttonbox)
		gobalbox.Add(buttonpanel, 0, wx.EXPAND | wx.ALL, 5)

		gobalpanel.SetSizer(gobalbox)
		self.Centre()

	def OnConvert(self, e):
		#dlg = wx.MessageDialog(self, message = ed2kConvert.ConvertLink(self.inputtext.GetLineText(0)), caption = u'Oops!', style = wx.OK)
		#dlg = wx.MessageDialog(self, message = self.inputtext.GetLineText(0), caption = str(self.inputtext.GetNumberOfLines()), style = wx.OK)
		#dlg.ShowModal()
		#dlg.Destroy()
		#
		self.resulttext.Clear()
		for i in range(self.inputtext.GetNumberOfLines()):
			self.resulttext.write(ed2kConvert.ConvertLink(self.inputtext.GetLineText(i)) + '\n')

	def OnAbout(self, e):
		""" Print Adout Dialog"""
		#AboutMsg = "ed2k Link Converter \n in wxPython"
		#AboutTitle = "About ed2k Link Converter"
		#dlg = wx.MessageDialog(self, AboutMsg, AboutTitle, wx.OK)
		#dlg.ShowModal()
		#dlg.Destroy()
		aboutdlginfo = wx.AboutDialogInfo()
		aboutdlginfo.AddDeveloper(u'Wei-Jie Hsiao (a.k.a. RJ)')
		aboutdlginfo.SetCopyright(u'Copyright @ 2010 Wei-Jie Hsiao')
		#aboutdlginfo.SetIcon(self, self.Icon)
		aboutdlginfo.SetLicence(u'licence GPL')
		aboutdlginfo.SetName(u'ed2k Link Converter')
		aboutdlginfo.SetVersion(u'version 0.1')
		aboutdlginfo.SetWebSite(u'http:www.google.com.tw')
		wx.AboutBox(aboutdlginfo)

	def OnExit(self, e):
		self.Close(True)

def RunGUI():
	app = wx.App()
	GUIWindow(None, wx.ID_ANY).Show(True)
	app.MainLoop()


