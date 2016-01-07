# -*- coding: utf-8 -*-
'''
Created on 2014年4月23日
Version:V1.0
@author:Liuxu
'''
import threading
import socket
from socket import AF_INET,SOCK_STREAM

con = threading.Condition()
HOST = raw_input("输入服务器IP地址：  ")
PORT = 8888
data = ''

s = socket.socket(AF_INET,SOCK_STREAM)  #创建套接字，绑定套接字到本地IP与端口:2014.4.24 15:40
print 'Socket 已创建'
s.bind((HOST, PORT))                    #套接字绑定的IP与端口(HOST,PORT)
s.listen(10)                            #开始监听连接s.listen()
print 'Socket 正在运行'


def clientThreadIn(conn, nick):         #conn.recv 
    global data
    while True:
        try:
            temp = conn.recv(1024)      #把接收到的数据实例化
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print data
        except:
            NotifyAll(nick + "离开房间!")
            print data
            return


def NotifyAll(sss):                    #con.notifyAll
    global data
    if con.acquire():
        data = sss
        con.notifyAll()
        con.release()
 
def ClientThreadOut(conn, nick):       #conn.send & conn.release
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
    conn, addr = s.accept()                     #进入循环，不断接受客户端的连接请求s.accept()
    print '连接到 ' + addr[0] + ':' + str(addr[1])
    nick = conn.recv(1024)                      #接收传来的数据，并发送给对方数据 conn.recv & notifyAll
    NotifyAll('欢迎 ' + nick + ' 来到房间!')
    print data
    print str((threading.activeCount() + 1) / 2) + ' person(s)!'
    conn.send(data)
    threading.Thread(target = clientThreadIn , args = (conn, nick)).start()
    threading.Thread(target = ClientThreadOut , args = (conn, nick)).start()

s.close()                                       #传输完毕后，关闭套接字 s.close())