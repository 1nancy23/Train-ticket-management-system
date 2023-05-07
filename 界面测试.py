from tkinter import *
import tkinter.messagebox

class LoginUi:
    def __init__(self,window,ALL):
        self.window = window
        self.System=ALL
    #初始化窗口
    def initWindow(self):
        self.width = 400
        self.height = 200
        #设置窗口宽高和位子
        self.window.geometry("%dx%d+%d+%d" % (self.width, self.height,
                                              (self.window.winfo_screenwidth() - self.width)/2,
                                              (self.window.winfo_screenheight()-self.height)/2))
        #标题
        self.window.title("登录窗口")
        #标签
        self.userNameLabel = Label(self.window, text="身份证：")
        self.userNameLabel.grid(row=0, column=1, columnspan=1)
        #输入框
        self.userNameEntry = Entry(self.window, bd=5)
        self.userNameEntry.grid(row=0, column=2, columnspan=1)

        self.passwordLabel = Label(self.window, text="密码：")
        self.passwordLabel.grid(row=1, column=1, columnspan=1)
        self.passwordEntry = Entry(self.window, bd=5)
        self.passwordEntry.grid(row=1, column=2, columnspan=1)
        #按钮
        self.checkButton = Button(self.window, text="登录", command=self.checkCallBack)
        self.checkButton.grid(row=2, column=1, columnspan=1)
        self.checkButton=Button(self.window,text="注册",command=self)

    def register(self):
        self.userNameEntry.get()==""

    def checkCallBack(self):

        if self.userNameEntry.get() == "" or self.passwordEntry.get() == "":
            tkinter.messagebox.showinfo('提示','请输入帐号或者密码！')

        if self.userNameEntry.get() in self.System.Persons.keys() and str(self.passwordEntry.get()) == self.System.Persons[self.userNameEntry.get()].password:
            tkinter.messagebox.showinfo('提示','密码正确！')
        else:
            tkinter.messagebox.showinfo('提示', '密码错误！')

from Try1_2 import Init
def login():
    System=Init()

    loginWindow = Tk() #创建窗口
    window = LoginUi(loginWindow,System) #类初始化
    window.initWindow() #窗口添加组件
    loginWindow.mainloop() #载入窗口循环


login()