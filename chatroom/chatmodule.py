#!/usr/bin/python
# -*- coding:utf-8 -*-

known = {'你好' : '你好呀!' ,'嗨' : '你好哦'}
history = []
print '你好, 我是Chatbot，跟我聊天吧!'
while True:
    inputed = raw_input('>>>')
    temp = ''
    for i in inputed:
        if i != ',' and i != '.' and i != '!' and i != '?':
            temp = temp + str(i).lower()
    if temp == 'show known' or temp == 'show history':
        if temp == 'show known':
            print
            print '我知道:'
            for i in known:
                print '    如果你说 \'' + i + '\', 我就说 \'' + known[i] + '\''
        else:
            print '聊天记录:'
            for i in history:
                print '    ' + i
            print
    else:
        history.append('User: ' + inputed)
        inputed = False
        for i in known:
            if temp.endswith(i):
                inputed = i
        if inputed != False:
            print known[inputed]
            history.append('Chatbot: ' + known[inputed])
        else:
            print '糟糕，我不知道怎么回答，我应该说什么呢?'
            appr = raw_input('<<<')
            known[temp] = appr
            history.append('Chatbot不知道说什么，你说应该回答 \'' + appr + '\' 。')
            print 'ok，我明白了。'