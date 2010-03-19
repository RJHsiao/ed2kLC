#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the GUI part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/03/18
# Version: 0.1

### Program Start
import wx

class GUIWindow(wx.Frame):
    """The GUI Window"""
    #def __init__(self, parent, id, title, pos, size, style):
    def __init__(self, parent, id):
        Title = 'ed2k Link Converter'
        InputLabel = "Input Links"
        ResultLabel = "Result"
        Pos = wx.DefaultPosition
        Size = (500,700)
        Style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        
        wx.Frame.__init__(self, parent, id, title = Title, pos = Pos, size = Size, style = Style)
        
        #self.control = wx.Panel(self)
        #labelInput = wx.StaticText()
        #textResult = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        #labelResult
        #textInput
    
    def OnAbout(self, e):
        AboutMsg = "ed2k Link Converter \n in wxPython"
        AboutTitle = "About ed2k Link Converter"
        dlg = wx.MessageDialog(self, AboutMsg, AboutTitle, wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnExit(self,e):
        self.Close(True)

def RunGUI():
    app = wx.App()
    #GUIWindow(None, wx.ID_ANY, title = Title, pos = Pos, size = Size, style = Style).Show(True)
    GUIWindow(None, wx.ID_ANY).Show(True)
    app.MainLoop()

#RunGUI()

