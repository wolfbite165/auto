from tkinter import *
import socket
import sys
import threading
import time


class Client1:
    def __init__(self):
        self.client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client1.connect(('192.168.31.150', 9980))
        self.start1()

    def __del__(self):
        self.client1.close()

    def start1(self):
        self.init1 = Tk()
        self.init1.title("客户端聊天工具")
        self.init1.geometry('500x500+500+500')
        self.text1 = Text(self.init1, width=60, height=20)
        self.text1.place(x=20, y=50)
        self.w = Label(self.init1, text="客户端信息框", width=60)
        self.w.place(x=20, y=20)
        self.bu = Button(self.init1, text="发送", command=self.add1)
        self.bu.place(x=20, y=430)
        self.text2 = Text(self.init1, width=25, height=3)
        self.text2.place(x=80, y=430)
        self.init1.after(1000, self.get2)
        self.init1.mainloop()

    def get2(self):
        t = threading.Thread(target=self.get1)
        t.setDaemon(True)
        t.start()
        self.init1.after(1000, self.get2)

    def get1(self):
        msg = self.client1.recv(1024)
        if msg is not None:
            msg = msg.decode('utf-8')
            self.text1.insert("end", "服务端发来的消息:" + msg + "\n")

    def add1(self):
        temp = self.text2.get(1.0, "end")
        temp1 = temp
        self.client1.send(temp1.encode('utf-8'))
        self.text1.insert("end", "你发送的消息:" + temp + "\n")
        self.text2.delete(1.0, "end")


a = Client1()