# -*- coding:utf-8 -*-
'''
Created on 2014年4月23日

@author: liuxu
'''

import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame (parent = None,title = '聊天室',size = (600,400))  #窗体大小设置
        panel = wx.Panel(frame,-1)
        
        button = wx.Button(panel,     #按钮
                           -1,
                           '发送',
                           pos = (505,340))
        
        lable1 = wx.StaticText(panel,-1,'对话框',pos = (280,10)) #对话框一
        text1 = wx.TextCtrl(panel,
                            -1,
                            pos = (10,30),
                            size = (580,220),
                            style = wx.TE_MULTILINE)

        lable2 =wx.StaticText(panel,-1,'Welcome to my chatroom!',pos = (10,320))  #对话框二
        text2 = wx.TextCtrl(panel,
                            -1,
                            pos = (10,260),
                            size = (580,50),
                            style = wx.TE_MULTILINE|wx.TE_RICH)
        
        text2.SetStyle(0,6,wx.TextAttr('red','blue'))
        frame.Show()
        return True
    
app = MyApp()
app.MainLoop()