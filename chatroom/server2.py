# -*- coding:utf-8 -*-
'''
Created on 2014年4月24日

@author: liuxu
'''

from gevent import socket
import gevent
import socket
import sys
import threading

con = threading.Condition()
Host = raw_input("input the server's ip adrress:")
PORT = 8888
data = ''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket creatde'
s.bind((HOST, PORT))
s.listen(10)
print 'Socket now listening'

def clientThreadIn(conn,nick):
    global data
    while True:
        try:
            temp = conn.recv(1024)
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print data
        except:
            NotifyAll(nick + "leavers the room!")
            print data
            return
        
def NotifyAll(sss):
    global data
    if con.acquire():
        data = sss
        con.notifyAll()
        con.release()

def ClientThreadOut(conn,nick):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return

while 1:
    conn,addr = s.accept()
    print 'Connected with ' + addr[0]
    nick = conn.recv(1024)
    NotifyAll('Welcome ' + nick + 'to the room!')
    print data
    print str((threading.activeCount() + 1)/2) + 'person(s)'
    conn.send(data)
    threading.Thread(target = clientThreadIn, args = (conn,nick).start)
    threading.Thread(target = ClientThreadOut,args = (conn,nick).start)
    
s.close()