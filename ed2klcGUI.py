#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ed2k Link Converter - the GUI part
# Auther Name: Wei-Jie Hsiao (a.k.a. RJ or RJ Hsiao, RJking, RJ-king)
# Date: 2010/30/18
# Version: 0.1

### Program Start
import wx

class GUIWindow(wx.Frame):
    """The GUI Window"""
    def __init__(self, parent, id, title, pos, size, style):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)

def RunGUI():
    Title = 'ed2k Link Converter'
    Pos = wx.DefaultPosition
    Size = wx.DefaultSize
    Style = wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX

    app = wx.App()
    GUIWindow(None, wx.ID_ANY, title = Title, pos = Pos, size = Size, style = Style).Show(True)
    app.MainLoop()

#RunGUI()

