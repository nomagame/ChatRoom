# -*- coding:utf-8 -*-
'''
Created on 2014年4月23日

@author: liuxu
'''
import wx
class myapp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title = '登录',size = (300,200))
        
        panel = wx.Panel(frame,-1)
        
        button2 = wx.Button(panel,
                            -1,
                            '连接',
                            pos = (140,100))
       
        label3 = wx.StaticText(panel,-1,'Chatroom',pos = (147,20))
        label4 = wx.StaticText(panel,-1,'客户端IP地址',pos = (10,55))
        
        text = wx.TextCtrl(panel,
               -1,
               pos = (100,50),
               size = (160,-1))

        frame.Show()
        return True
    
app = myapp()
app.MainLoop()