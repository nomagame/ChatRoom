# -*- coding: utf-8 -*-
'''
Created on 2014年4月23日

@author: liuxu
'''
from gevent import socket
import AF_INET,SOCK_STREAM
import threading

inString = ''
outString = ''
nick = ''

def DealOut(s):
    global nick, outString
    while True:
        outString = raw_input()
        outString = nick + ': ' + outString
        s.send(outString)

def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break

nick = raw_input("请输入用户名: ")
ip = raw_input("输入服务器IP地址: ")
sock = socket.socket(AF_INET,SOCK_STREAM)
sock.connect((ip, 8888))
sock.send(nick)

thin = threading.Thread(target = DealIn, args = (sock,))
thin.start()
thout = threading.Thread(target = DealOut, args = (sock,))
thout.start()
