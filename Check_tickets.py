import random
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import operator
import Interface_testing
'''
class LoginUi:
    def __init__(self, window):
        self.loginWindow = window
        self.loginWindow.config()
        Check_tickets(self.loginWindow)'''

class Check_tickets():
    def __init__(self, window):
        # 列表
        def show(event):
            object = event.widget
            index = object.curselection()
            # index是返回的从0开始的第几行的数
            var.set(object.get(index))
            window_temp = tk.Tk()
            window_temp.title("购买火车票")
            window_temp.geometry('250x70')
            Text2 = Label(window_temp, text="是否选择购买此火车票？")
            Text2.place(x=60, y=5)
            self.Button_Search1 = Button(window_temp, text="确认", command=self.Check_Sure)
            self.Button_Search1.place(x=100, y=30)
        # 列表
        sc = tk.Scrollbar(window)
        sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        var = tk.StringVar()
        lb = tk.Listbox(window,height=20,width=40,borderwidth=3,yscrollcommand=sc.set)
        List_All = Interface_testing.list1
        print(List_All)
        for i in List_All:
            lb.insert(tk.END,i)
        lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # 滚动条动，列表跟着动
        sc.config(command=lb.yview)
        lb.bind("<<ListboxSelect>>", show)

    def Check_Sure(self,):
        tk.messagebox.showinfo('提示', '购票成功！')



def login1():
    print(1)
    loginWindow = tk.Tk()
    Check_tickets(loginWindow)
    loginWindow.mainloop()

login1()