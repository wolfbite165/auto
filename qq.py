from tkinter import *
import socket
import sys
import threading
import time
class Server1:
    def __init__(self):  #初始化创建socket套接字,并且调用start1方法绘制界面
        self.serv1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serv1.bind((socket.gethostname(),9980))
        self.serv1.listen(5)
        self.client,self.addr=self.serv1.accept()
        self.start1()
    def __del__(self): #析构函数,当程序退出时,执行该函数,主要是为了关闭创建的socket套接字
        self.serv1.close()
        self.client.close()
    def start1(self): #界面绘制
        self.init1=Tk()
        self.init1.title("服务端聊天工具")
        self.init1.geometry('500x500+500+500')
        self.text1=Text(self.init1,width=60,height=20)
        self.text1.place(x=20,y=50)
        self.w=Label(self.init1,text="服务端信息框",width=60)
        self.w.place(x=20,y=20)
        self.bu=Button(self.init1,text="发送",command=self.add1)
        self.bu.place(x=20,y=430)
        self.text2=Text(self.init1,width=25,height=3)
        self.text2.place(x=80,y=430)
        self.init1.after(1000,self.get2)  #这里调用了after方法,即隔一段时间执行事件
        self.init1.mainloop()
    def get2(self): #创建线程
        t=threading.Thread(target=self.get1)
        t.setDaemon(True)
        t.start()
        self.init1.after(1000,self.get2) #这里与上面的after方法一致,这样就能每隔一段时间执行
    def get1(self): #此函数是为了判断对方有没有发送消息,如果有,就在文本框显示对方发送的消息
        msg=self.client.recv(1024)
        if msg is not None:
            msg=msg.decode('utf-8')
            self.text1.insert("end","客户端发来的消息:" + msg + "\n")
    def add1(self): #这是按钮事件,即button点击事件,点击后,发送文本框消息
        temp=self.text2.get(1.0,"end")
        temp=temp
        self.client.send(temp.encode('utf-8'))
        self.text1.insert("end","你发送的消息:" + temp+ "\n")
        self.text2.delete(1.0,"end")


a=Server1()