import random
import tkinter as tk
from tkinter import *
import tkinter.messagebox
# from ttkbootstrap import Style
from tkinter import ttk
from PIL import ImageTk, Image
from time import time
from operator import mul
from string import ascii_letters, digits
from random import choice, choices, randrange
from PIL import Image, ImageDraw, ImageFont, Image
# import Feature_summary_administrator as Fa
# import Feature_summary_user as Fu
import operator
from Try1_2_04_17 import Init, Person, Train, Station, AllTrain

System = Init()


class LoginUi:
    def __init__(self, window):
        self.loginWindow = window
        self.loginWindow.config()
        chooseWindow(self.loginWindow)


class chooseWindow():
    # 管理员、用户选择登陆
    def __init__(self, window):
        self.window = window
        self.window.title("官网登陆")
        self.window.geometry("960x700+300+60")
        #style = Style(theme='united')
        #self.window = style.master
        #self.width = 225
        #self.height = 100
        canvas = tk.Canvas(window, width=960, height=700, bd=0, highlightthickness=0)
        imgpath = './image/background1.jpg'
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(480, 470, image=photo)
        # 设置窗口宽高和位子
        #self.window.geometry("%dx%d+%d+%d" % (self.width, self.height,
        #                                      (self.window.winfo_screenwidth() - self.width) / 2,
        #                                      (self.winZSWdow.winfo_screenheight() - self.height) / 2))
        # 标题
        canvas.create_text(450, 120, text="欢迎进入12306火车票购票系统", font=("宋体", 35))
        canvas.create_text(700,400, text="请选择管理员或者用户登录",font=("宋体",20))
        canvas.pack()
        self.administratorButton = Button(self.window, text="管理员", command=self.administrator,font=("宋体",13), bg="grey")
        self.administratorButton.place(x=620,y=460)
        self.userButton = Button(self.window, text="用户", command=self.user,font=("宋体",13), bg="grey")
        self.userButton.place(x=720,y=460)
        window.mainloop()
        '''
        self.chooseLabel.grid(row=0, column=1, columnspan=1)
        # 按钮1
        self.administratorButton = Button(self.window, text="管理员", command=self.administrator)
        self.administratorButton.grid(row=2, column=1, columnspan=1)
        # 按钮2
        self.userButton = Button(self.window, text="用户", command=self.user)
        self.userButton.grid(row=2, column=2, columnspan=1)
        '''


    def administrator(self):
        global val  # 标记管理员与用户的选择：0为用户，1为管理员
        val = 1
        self.window.destroy()
        window = tk.Tk()
        initWindow(window)

    def user(self):
        global val
        val = 0
        self.window.destroy()
        window = tk.Tk()
        initWindow(window)


class initWindow():
    # 初始化窗口
    def __init__(self, window):
        self.window = window
        self.window.title("官网登陆")
        self.window.geometry("760x500+350+100")
        canvas = tk.Canvas(window, width=760, height=500, bd=0, highlightthickness=0)
        imgpath = './image/background2.jpg'
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(480, 289, image=photo)
        canvas.pack()
        # 标签
        canvas.create_text(273, 115, text="帐号：", font=("宋体"))
        # 输入框
        self.userNameEntry = Entry(self.window, bd=5)
        self.userNameEntry.place(x=343, y=100)

        canvas.create_text(273, 215, text="密码：", font=("宋体"))
        self.passwordEntry = Entry(self.window, bd=5)
        self.passwordEntry.place(x=343, y=200)
        # 按钮1
        self.checkButton = Button(self.window, text="登录", command=self.checkCallBack, font=("宋体", 13), bg="grey")
        self.checkButton.place(x=250, y=306)
        # 按钮2
        self.checkButton = Button(self.window, text="注册", command=self.enroll, font=("宋体", 13), bg="grey")
        self.checkButton.place(x=350, y=306)
        # 按钮3
        self.checkButton = Button(self.window, text="返回", command=self.back, font=("宋体", 13), bg="grey")
        self.checkButton.place(x=450, y=306)

        window.mainloop()

    def checkCallBack(self):
        if self.userNameEntry.get() == "" or self.passwordEntry.get() == "":
            tkinter.messagebox.showinfo('提示', '请输入帐号或者密码！')
        if self.userNameEntry.get() != "":
            try:
                Person1 = System.Persons[self.userNameEntry.get()]
                if self.passwordEntry.get() == Person1.password:
                    tkinter.messagebox.showinfo('提示', '密码正确！正在登录中……')
                    self.change(Person1)  # 跳转页面
                else:
                    tk.messagebox.showerror('提示', '密码错误')
            except:pass
                # print("assss")
                # tkinter.messagebox.showinfo('提示','用户不存在')


    def enroll(self):
        self.window.destroy()
        window = tk.Tk()
        enroll(window)

    def back(self):
        self.window.destroy()
        window = tk.Tk()
        chooseWindow(window)

    def change(self, Person1):
        self.window.destroy()
        window = tk.Tk()

        if (val):
            choose1(window, Person1)  # 管理员
        else:
            choose2(window, Person1)  # 用户


# 注册界面
class enroll():
    # 注册
    def __init__(self, window):
        self.window = window
        self.window.title("注册")
        self.window.geometry("760x500+300+60")
        canvas = tk.Canvas(window, width=760, height=500, bd=0, highlightthickness=0)
        imgpath = './image/background2.jpg'
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(480, 289, image=photo)
        canvas.pack()
        # 用户名
        canvas.create_text(273, 55, text="用户名：", font=("宋体"))
        self.userNameEntry = Entry(self.window, bd=5)
        self.userNameEntry.place(x=343, y=40)
        # 身份证号
        canvas.create_text(273, 125, text="身份证号：", font=("宋体"))
        self.useridEntry = Entry(self.window, bd=5)
        self.useridEntry.place(x=343, y=110)
        # 手机号
        canvas.create_text(273, 195, text="手机号：", font=("宋体"))
        self.userNumberEntry = Entry(self.window, bd=5)
        self.userNumberEntry.place(x=343, y=180)
        # 密码
        canvas.create_text(273, 265, text="密码：", font=("宋体"))
        self.usercodeEntry = Entry(self.window, bd=5)
        self.usercodeEntry.place(x=343, y=250)
        # 再次确认密码
        canvas.create_text(273, 335, text="再次确认密码：", font=("宋体"))
        self.usercode1Entry = Entry(self.window, bd=5)
        self.usercode1Entry.place(x=343, y=320)
        # 注册
        self.userButton = Button(self.window, text="注册", command=self.retranslate, font=("宋体", 13), bg="grey")
        self.userButton.place(x=300, y=380)
        # 返回
        self.userButton = Button(self.window, text="返回", command=self.back, font=("宋体", 13), bg="grey")
        self.userButton.place(x=400, y=380)
        window.mainloop()
        ''''# 请输入验证码
        self.userNameLabel = Label(self.window, text="请输入验证码：")
        self.userNameLabel.grid(row=5, column=1, columnspan=1)
        self.userNameEntry = Entry(self.window, bd=5)
        self.userNameEntry.grid(row=5, column=2, columnspan=1)
        # 显示验证码图片和标签组件
        lbImange = tk.Label(window)
        lbImange.place(x=10,y=10,width=330,height=110)
        # 验证码图片中的候选字符集
        characters = ascii_letters + digits
        # 当前验证码字符串
        code = tk.StringVar(window,value='')
        # 最后一个验证码生成的时间
        startTime = tk.IntVar(window,value=0)
        def getColor():
            # 生成随机色彩
            return tuple(choices(range(200),k=3))
        def showImage(event=None,size=(320,100),characterNumber=6,bgcolor=(255,255,255)):
            imageTemp = Image.new('RGB',size,bgcolor)
            draw = ImageDraw.Draw(imageTemp)
            text = ''.join(choices(characters,k=characterNumber))
            code.set(text)
            font = ImageFont.truetype()
            if width+2*characterNumber>size[0] or height>size[1]:
                print('尺寸不合法')
                return'''

    def retranslate(self):

        # 身份证验证
        if len(self.useridEntry.get()) != 18:
            tk.messagebox.showerror('失败', '注册失败，身份证号码错误！')

        elif not (self.userNumberEntry.get().isdigit() and len(self.userNumberEntry.get()) == 11):
            tk.messagebox.showerror('失败', '注册失败，手机号不正确！')
        elif len(self.usercodeEntry.get()) < 8:
            tk.messagebox.showerror('失败', '注册失败，密码位数小于8位！')
        elif not (any([x.isdigit() for x in self.usercodeEntry.get()]) and
                  any([x.isalpha() for x in self.usercodeEntry.get()])):
            tk.messagebox.showerror('失败', '注册失败，密码格式错误，必须包括字母和数字以及特殊符号！')
        elif self.usercodeEntry.get() != self.usercode1Entry.get():
            tk.messagebox.showerror('失败', '注册失败，两次密码不相同！')
        else:
            try:
                A = System.Persons[self.useridEntry.get()]  ###已经存在
                tk.messagebox.showinfo('不成功', '已经注册！')
            except:
                Person1 = Person(System, self.userNameEntry.get(), self.useridEntry.get(), self.userNumberEntry.get(),
                                 self.usercodeEntry.get(), False)
                System.Add_Person(Person1)
                tk.messagebox.showinfo('成功', '注册成功！')
            # 这里就可以将新用户存入数据库中

    def back(self):
        self.window.destroy()
        window = tk.Tk()
        initWindow(window)


# 选择功能界面 管理员
class choose1():
    def __init__(self, window, Person1):
        print(val)
        self.Person1 = Person1
        self.window = window
        self.window.title("办事大厅")
        self.window.geometry("800x250+310+190")
        canvas = tk.Canvas(self.window, width=800, height=250, bd=0, highlightthickness=0)
        imgpath = './image/background4.jpg'
        global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 125, image=photo)
        canvas.pack()

        # 用户管理
        self.checkButton1 = Button(self.window, text="用户管理", command=self.Contrl_Uesr, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton1.place(x=100, y=50)
        # 车站管理
        self.checkButton2 = Button(self.window, text="车次管理", command=self.Contrl_Station, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton2.place(x=200, y=50)
        # 车次查询
        self.checkButton2 = Button(self.window, text="车次查询", command=self.Contrl_Train, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton2.place(x=100, y=120)
        # 设置返回键
        self.btn_back = tk.Button(self.window, text='返回', command=self.back, relief=GROOVE, bg='aliceblue')
        self.btn_back.place(x=200, y=120)

        self.choose = tk.Frame(self.window, )
        self.choose.pack()

    def Contrl_Uesr(self):    # 用户管理
        window_temp=tk.Tk()
        Text1=Label(window_temp,text="所有用户");Text1.grid(row=1,column=1)
        List_Person=self.Person1.System.Return_Person()
        print(List_Person)
        List_Button=[]

        for i in range(len(List_Person)):
            List_Button.append(Button(window_temp,text=str(List_Person[i])))
            List_Button[i].grid(row=i+1,column=1)

    def Contrl_Train(self):   # 车次管理
        List_Train = self.Person1.System.Return_Train()
        '''+
        window_temp=tk.Tk()
        Text1=Label(window_temp,text="所有车辆");Text1.grid(row=1,column=1)
        List_Train=self.Person1.System.Return_Train()
        #List_Button=[]
        def Get_Detail_Train(i):
            window_temp_new=tk.Tk()
            List_Button2=[]
            Times=list(List_Train[i][1].keys())
            Stations=list(List_Train[i][1].values())
            for m in range(len(Times)):
                List_Button2.append(Label(window_temp_new,text=str(Times[m])+str(Stations[m])))
                List_Button2[m].grid(row=m,column=1)
        for i in range(len(List_Train)):
            List_Button.append(Button(window_temp,text=str(List_Train[i][0]),command=lambda:Get_Detail_Train(i)))
            List_Button[i].grid(row=i+1,column=1)
            '''

        # 车次删除与添加
        def show(event):
            object = event.widget
            index = object.curselection()
            # index是返回的从0开始的第几行的数
            var.set(object.get(index))
            window_temp = tk.Tk()
            window_temp.title("车次的删除")
            window_temp.geometry('250x70')
            Text2 = Label(window_temp, text="是否删除该车次？")
            Text2.place(x=70, y=5)
            self.Button_Search1 = Button(window_temp, text="确认", command=delete)
            self.Button_Search1.place(x=100, y=30)
            window_temp.mainloop()
        def delete():
            index = lb.curselection()
            if len(index) == 0:
                return
            lb.delete(index)
        def add():
            add_window = tk.Tk()
            add_window.title("添加车次信息")
            Sequence_number = tk.Label(add_window, text="请输入添加车次序号：");Sequence_number.grid(row=0, column=0, padx=5, pady=5)
            addnumber_entry = tkinter.Entry(add_window);addnumber_entry.grid(row=0, column=1, padx=5, pady=5)
            Departure_station = tk.Label(add_window, text="请输入出发站名：");Departure_station.grid(row=2, column=0, padx=5, pady=5)
            addstation_entry = tk.Entry(add_window);addstation_entry.grid(row=2, column=1, padx=5, pady=5)
            Arrival_station = tk.Label(add_window, text="请输入到达站名：");Arrival_station.grid(row=3, column=0, padx=5, pady=5)
            Arrival_sentry = tk.Entry(add_window);Arrival_sentry.grid(row=3, column=1, padx=5, pady=5)
            departure_time = tk.Label(add_window, text="请输入出发时间：");departure_time.grid(row=4, column=0, padx=5, pady=5)
            departure_entry = tk.Entry(add_window);departure_entry.grid(row=4, column=1, padx=5, pady=5)
            Arrival_time = tk.Label(add_window, text="请输入到达时间：");Arrival_time.grid(row=5, column=0, padx=5, pady=5)
            Arrival_entry = tk.Entry(add_window);Arrival_entry.grid(row=5, column=1, padx=5, pady=5)
            addbutton = tk.Button(add_window, text="确认添加",command=add_sure)
            addbutton.grid(row=6, column=1, padx=5, pady=5)
        def add_sure():
            getn = self.addnumber_entry.get()
            getds = self.addstation_entry.get()
            getas = self.Arrival_sentry.get()
            getdt = self.departure_entry.get()
            getat = self.Arrival_entry.get()
            varAdd = getn + getds + getas + getdt + getat
            if (len(varAdd.strip())) == 0:
                return
            lb.insert(tkinter.END, varAdd)

            # !!!!!这里还有添加在后端进行添加的代码

        # 列表
        loginWindow = tk.Tk()
        loginWindow.title("车次查询")
        # 添加添加按钮
        #buttonAdd = tkinter.Button(loginWindow, text='增加车次', width=10, command=add)
        #buttonAdd.grid(row=0, column=1, padx=5, pady=5)
        sc = tk.Scrollbar(loginWindow)
        sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        var = tk.StringVar()
        lb = tk.Listbox(loginWindow, height=20, width=40, borderwidth=3, yscrollcommand=sc.set)
        for i in List_Train:
            lb.insert(tk.END, i)
        lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        # 鼠标右键事件
        def callback(event):
            print("clicked at:",event.x,event.y)
            call = tk.Tk()
            call.geometry('250x70')
            call.title("添加新车次")
            label = tk.Label(call, text='是否新添加车次')
            label.place(x=85, y=5)
            buttonAdd = tkinter.Button(call, text='确定', width=10, command=add)
            buttonAdd.place(x=90, y=30)
            call.mainloop()

        loginWindow.bind("<Button-3>", callback)
        # 滚动条动，列表跟着动
        sc.config(command=lb.yview)
        lb.bind("<<ListboxSelect>>", show)


        # 添加

        '''
        Button_Search = Button(window_temp, text="查询", command=Get_S)
        Button_Search.grid(row=5, column=1)
        Get_Buy = Entry(window_temp)
        Get_Buy.grid(row=5, column=3)
        '''

    def Contrl_Station(self):   # 车站查询
        window_temp=tk.Tk()
        Text=Label(window_temp,text="所有车站");Text.grid(row=1,column=1)
        List_Station=self.Person1.System.Return_Station()
        pass

    def back(self):
        self.window.destroy()
        window = tk.Tk()
        initWindow(window)
        '''
    def User_management(self):
        Fa.

    def Ticket_inquiry(self):
        Fa.

    def Train_management(self):
        Fa.

    def Station_inquiry(self):
        Fa.

    def Booking(self):
        Fa.

    def Return_a_ticket(self):
        Fa.
        '''
from Change_Button import Change_Tickt
# 选择功能界面 用户
class choose2():
    def __init__(self, window, Person1):
        print(val)
        self.Person1 = Person1
        self.window = window
        self.window.title("办事大厅")
        self.window.geometry("800x250+310+190")
        canvas = tk.Canvas(self.window, width=800, height=250, bd=0, highlightthickness=0)
        imgpath = './image/background4.jpg'
        global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)

        canvas.create_image(400, 125, image=photo)
        canvas.pack()
        canvas.create_text(180, 24, text="欢迎使用12306购票系统", font=("宋体"))
        canvas.create_text(273, 180, text="更多功能敬请期待！", font=("宋体"))
        # 车票查询
        self.checkButton1 = Button(self.window, text="按车票查询", command=self.Search_T1, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton1.place(x=100, y=50)
        # 车站查询
        self.checkButton3 = Button(self.window, text="按车站查询", command=self.Search_S1, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton3.place(x=200, y=50)
        # 订票
        self.checkButton4 = Button(self.window, text="查询已订票", command=self.Find1, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton4.place(x=100, y=120)
        # 退票
        self.checkButton5 = Button(self.window, text="退票", command=self.Return_a_ticket1, relief=GROOVE,
                                   bg='ghostwhite')
        self.checkButton5.place(x=200, y=120)
        self.checkButton6 = Change_Tickt(self.Person1, self.window, 300, 50)

        self.checkButton6=Button(self.window,text="返回",command=self.back, relief=GROOVE, bg='aliceblue')
        self.checkButton6.place(x=750,y=200)
        self.choose = tk.Frame(self.window, )
        self.choose.pack()
    def Search_T1(self):
        self.window.destroy()
        window = tk.Tk()
        self.Search_T(window)
    def Find1(self):
        self.window.destroy()
        window = tk.Tk()
        self.Find(window)
    def Return_a_ticket1(self):
        self.window.destroy()
        window = tk.Tk()
        self.Return_a_ticket(window)
    def Search_S1(self):
        self.window.destroy()
        window = tk.Tk()
        self.Search_S(window)

    def Return_a_ticket(self,window):
        window_temp3 = window
        window_temp3.title("退票")
        window_temp3.geometry("800x250+310+190")
        canvas = tk.Canvas(window_temp3, width=800, height=250, bd=0, highlightthickness=0)
        imgpath = './image/background5.jpg'
        global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 125, image=photo)
        canvas.pack()
        canvas.create_text(130, 20, text="请输入要进行退票的车次名", font=("宋体", 12))
        canvas.create_text(130, 50, text="（-.-）=3  （。o。）~@  # # ", font=("宋体", 12))
        canvas.create_text(73, 105, text="退票车次名", font=("宋体", 12))
        canvas.create_text(73,130,text='退票身份证',font=("宋体",12))
        Get2=Entry(window_temp3,bd=5)
        Get2.place(x=143,y=130)
        Get1 = Entry(window_temp3, bd=5)
        Get1.place(x=143, y=90)
        def back():
            window_temp3.destroy()
            window = tk.Tk()
            choose2(window,self.Person1)
        def Back_Buy():
            print("123",Get1.get().replace(" ",''))
            self.Person1.Back_Tickt(Get2.get(),Get1.get())
            tkinter.messagebox.showinfo('退票', '退票成功！')
        Button1=Button(window_temp3,text='确定',command=Back_Buy, font=("宋体", 12),relief=GROOVE, bg='aliceblue')
        Button1.place(x=120,y=180)
        Button2 = Button(window_temp3, text='返回', command=back, font=("宋体", 12), relief=GROOVE, bg='aliceblue')
        Button2.place(x=200, y=180)
    def Find(self,window):
        window_temp2 = window
        window_temp2.title("查询已订票")
        window_temp2.geometry("800x250+310+190")
        canvas = tk.Canvas(window_temp2, width=800, height=250, bd=0, highlightthickness=0)
        imgpath = './image/background5.jpg'
        global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 125, image=photo)
        canvas.pack()
        canvas.create_text(150, 20, text="请输入要进行查询车票人的身份证号码", font=("宋体", 12))
        canvas.create_text(156, 50, text="\*^0^*/~  \*^@^*/~  /（^v^）\~  ~ ~~", font=("宋体", 12))
        canvas.create_text(73, 105, text="身份证号码", font=("宋体", 12))
        Get1 = Entry(window_temp2, bd=5);
        Get1.place(x=143, y=90)

        def back():
            window_temp2.destroy()
            window = tk.Tk()
            choose2(window,self.Person1)

        def get_find():
            Information = self.Person1.Return_tickts(Get1.get())
            print(Information)
            Text2=Label(window_temp2,text=Information)
            Text2.place(x=200,y=100)
        Button1=Button(window_temp2,text='查询', font=("宋体", 12),command=get_find, relief=GROOVE, bg='aliceblue');Button1.place(x=140,y=150)
        Button2 = Button(window_temp2, text='返回', font=("宋体", 12), command=back, relief=GROOVE, bg='aliceblue');
        Button2.place(x=210, y=150)


        # print(Information)
    def Search_T(self,window):
        Stations = "所有站台:" + str((list(System.Stations.keys())))
        print(Stations)
        window_temp = window
        window_temp.title("车票查询")
        window_temp.geometry("800x250+310+190")
        canvas = tk.Canvas(window_temp, width=800, height=250, bd=0, highlightthickness=0)
        imgpath = './image/background5.jpg'
        global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 125, image=photo)
        canvas.pack()

        canvas.create_text(340, 20, text=Stations)

        canvas.create_text(73, 55, text="选择日期", font=("宋体",10))
        Get2 = Entry(window_temp, bd=5);
        Get2.place(x=143, y=40)

        canvas.create_text(73, 105, text="出发站", font=("宋体",10))
        Get3 = Entry(window_temp, bd=5);
        Get3.place(x=143, y=90)

        canvas.create_text(73, 155, text="终点站", font=("宋体",10))
        Get4 = Entry(window_temp, bd=5);
        Get4.place(x=143, y=140)

        List_All = []
        List_All1 = []
        def Get_S():
            if '' in [Get2.get(), Get3.get(), Get4.get()]:
                tk.messagebox.showerror('提示', '请填写完整')
            else:
                Dict_ = self.Person1.Search_by_DAY(Get2.get(), Get3.get(), Get4.get())
                print(Dict_)
                List_All1.extend(Dict_)
                for j in List_All1:
                    List_All2 = []
                    for i in range(6):
                        if (i != 3):
                            List_All2.append(j[i])
                        if (i == 3):
                            List_All2.append(j[i][0])
                            List_All2.append(j[i][1])
                    List_All.append(List_All2)

                def Check_Sure(window):
                    window_temp_new = window
                    window_temp_new.title("座位选择")
                    window_temp_new.geometry("460x240+500+250")
                    canvas = tk.Canvas(window_temp_new, bd=0, highlightthickness=0)
                    imgpath = './image/background7.jpg'
                    global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
                    img = Image.open(imgpath)
                    photo = ImageTk.PhotoImage(img)
                    canvas.create_image(217, 70, image=photo)
                    canvas.pack()
                    A1 = tk.IntVar()
                    A2 = tk.IntVar()
                    A3 = tk.IntVar()
                    A4 = tk.IntVar()
                    A5 = tk.IntVar()

                    def toggle(var):
                        var.set(not var.get())

                    Checkbutton1 = Checkbutton(window_temp_new, text="A座", command=lambda: toggle(A1))
                    Checkbutton1.place(x=80, y=115)
                    Checkbutton2 = Checkbutton(window_temp_new, text="B座", command=lambda: toggle(A2))
                    Checkbutton2.place(x=130, y=115)
                    Checkbutton3 = Checkbutton(window_temp_new, text="C座", command=lambda: toggle(A3))
                    Checkbutton3.place(x=180, y=115)
                    Checkbutton4 = Checkbutton(window_temp_new, text="D座", command=lambda: toggle(A4))
                    Checkbutton4.place(x=270, y=115)
                    Checkbutton5 = Checkbutton(window_temp_new, text="F座", command=lambda: toggle(A5))
                    Checkbutton5.place(x=320, y=115)
                    Text1_1 = Label(window_temp_new, text='请输入购票人身份证号码')
                    Text1_1.place(x=60, y=150)
                    Text2 = Entry(window_temp_new)
                    Text2.place(x=210, y=150)

                    def Que():
                        Index = uu
                        site_y = [A1.get(), A2.get(), A3.get(), A4.get(), A5.get()].index(1)
                        print("此刻状态",List_All1)
                        self.Person1.Buy_Tickt(Text2.get(), List_All1[Index][0], List_All1[Index][1], List_All1[Index][2],
                                               List_All1[Index][3],
                                               [random.randint(0, 100), site_y],List_All1[Index][5])
                        tkinter.messagebox.showinfo('订票', '订票成功！')
                        Return()

                    def Return():
                        window_temp_new.destroy()
                        window = tk.Tk()
                        self.Search_T(window)

                    Button1 = Button(window_temp_new, text='确定', command=Que, relief=GROOVE);Button1.place(x=200, y=195)
                    # Button1.grid(row=3, column=2)
                    # Index = int(uu[0])
                    # self.Person1.Buy_Tickt(List_All[Index][0], List_All[Index][1], List_All[Index][2],
                    #                        List_All[Index][3],
                    #                        [random.randint(0, 5), random.randint(0, 4)])
                    #
                    # tkinter.messagebox.showinfo('订票', '订票成功！')
                    window_temp_new.mainloop()


                def show(event):
                    window_temp.destroy()
                    item = table.selection()
                    index = int(list(item)[0][1:4])-1
                    global uu
                    uu = index
                    print("uu_tedt",uu)
                    # index是返回的从0开始的第几行的数
                    window_temp0 = tk.Tk()
                    window_temp0.title("购买火车票")
                    window_temp0.geometry("500x240+500+250")
                    canvas = tk.Canvas(window_temp0, width=500, height=240, bd=0, highlightthickness=0)
                    imgpath = './image/background6.jpg'
                    global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
                    img = Image.open(imgpath)
                    photo = ImageTk.PhotoImage(img)
                    canvas.create_image(400, 125, image=photo)
                    canvas.pack()

                    def Check_Sure1():
                        window_temp0.destroy()
                        win.destroy()
                        window = tk.Tk()
                        Check_Sure(window)

                    time1 = List_All[uu][3]
                    time2 = List_All[uu][4]
                    train = List_All[uu][0]
                    money = List_All[uu][5]
                    Get31 = List_All[uu][1]
                    Get41 = List_All[uu][2]
                    text1 = '\n' + time1 + "           " + time2 + "\n" + "                  ——>" + \
                            "\n" + "              " + train + "    " + "￥" + str(money) + "    " + "\n" + '           ' + Get31 + "       " + Get41 + "\n"
                    canvas.create_text(255, 50, text=text1, font=("宋体"))
                    canvas.create_text(240, 140, text="是否选择购买此火车票?", font=("宋体"))
                    Button_Search = Button(window_temp0, text="确认",command=Check_Sure1, relief=GROOVE,
                                           bg='lightcyan', font=("宋体", 12))
                    Button_Search.place(x=220, y=180)
                    window_temp0.mainloop()


                def insert():
                    # 插入数据
                    info = List_All
                    for index, data in enumerate(info):
                        table.insert('', END, values=data)  # 添加数据到末尾
            win = tk.Tk()
            win.title('车票查询')  # 标题
            screenwidth = win.winfo_screenwidth()  # 屏幕宽度
            screenheight = win.winfo_screenheight()  # 屏幕高度
            width = 800
            height = 200
            x = int((screenwidth - width) / 2)
            y = int((screenheight - height) / 2)
            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

            tabel_frame = tkinter.Frame(win)
            tabel_frame.pack()

            xscroll = Scrollbar(tabel_frame, orient=HORIZONTAL)
            yscroll = Scrollbar(tabel_frame, orient=VERTICAL)

            columns = ['车次', '初始站', '到达站', '出发时间', '到达时间', '票价', '剩余票数']
            table = ttk.Treeview(
                master=tabel_frame,  # 父容器
                height=10,  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
                xscrollcommand=xscroll.set,  # x轴滚动条
                yscrollcommand=yscroll.set,  # y轴滚动条
            )
            for column in columns:
                table.heading(column=column, text=column, anchor=CENTER,
                                  command=lambda name=column:
                                  tk.messagebox.showinfo('', '{}描述信息~~~'.format(name)))  # 定义表头
                table.column(column=column, width=100, minwidth=100, anchor=CENTER, )  # 定义列
            xscroll.config(command=table.xview)
            xscroll.pack(side=BOTTOM, fill=X)
            yscroll.config(command=table.yview)
            yscroll.pack(side=RIGHT, fill=Y)
            table.pack(fill=BOTH, expand=True)
            insert()
            btn_frame = Frame()
            btn_frame.pack()
            #Button(btn_frame, text='添加', bg='yellow', width=20, command=insert).pack(side=LEFT)
            #Button(btn_frame, text='删除', bg='pink', width=20).pack(side=LEFT)
            table.bind('<ButtonRelease-1>', show)
            win.mainloop()

        def Back1():
            window_temp.destroy()
            window = tk.Tk()
            choose2(window, self.Person1)


        Button_Search = Button(window_temp, text="查询", command=Get_S, font=("宋体",10), relief=GROOVE, bg='aliceblue')
        Button_Search.place(x=160, y=195)
        Button_Search = Button(window_temp, text="返回", command=Back1, font=("宋体", 10), relief=GROOVE,
                               bg='aliceblue')
        Button_Search.place(x=220, y=195)
        window_temp.mainloop()

        def toggle(var):
            var.set(not var.get())
        # def Buy():
        #     window_temp_new=tk.Tk()
        #     A1=tk.IntVar();A2=tk.IntVar();A3=tk.IntVar();A4=tk.IntVar();A5=tk.IntVar()
        #     Checkbutton1=Checkbutton(window_temp_new,text="A座",variable=toggle(A1));Checkbutton1.grid(row=1,column=1)
        #     Checkbutton2=Checkbutton(window_temp_new,text="B座",variable=toggle(A2));Checkbutton2.grid(row=1,column=2)
        #     Checkbutton3=Checkbutton(window_temp_new,text="C座",variable=toggle(A3));Checkbutton3.grid(row=2,column=1)
        #     Checkbutton4=Checkbutton(window_temp_new,text="D座",variable=toggle(A4));Checkbutton4.grid(row=2,colmun=2)
        #     Checkbutton5=Checkbutton(window_temp_new,text="E座",variable=toggle(A5));Checkbutton5.grid(row=3,column=1)
        #     Text2 = Entry(window_temp_new, text='请输入购票人身份证号码')
        #     Text2.grid(row=4, column=1)
        #     def Que():
        #         Index = int(Get_Buy.get())
        #         self.Person1.Buy_Tickt(Text2,List_All[Index][0], List_All[Index][1], List_All[Index][2], List_All[Index][3],
        #                                [random.randint(0, 5), random.randint(0, 4)])
        #         tkinter.messagebox.showinfo('订票', '订票成功！')
        #     Button1=Button(window_temp_new,text='确定',command=Que);Button1.grid(row=3,column=2)
        #
        #
        #
        # Text_Q=Button(window_temp, text="若需买票请输入选第几个", command=Buy)
        # Text_Q.grid(row=5, column=2)
        #
        # window_temp.mainloop()

    def Search_S(self,window):
        Stations = "所有站台:" + str((list(System.Stations.keys())))
        window_temp = window
        window_temp.title("车站查询")
        window_temp.geometry("800x250+310+190")
        canvas = tk.Canvas(window_temp, width=800, height=250, bd=0, highlightthickness=0)
        imgpath = './image/background5.jpg'
        global photo  # 垃圾回收机制会回收图片，所以要使用全局变量
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 125, image=photo)
        canvas.pack()
        canvas.create_text(340, 20, text=Stations)
        canvas.create_text(73, 75, text="日期", font=("宋体", 10))
        Get2 = Entry(window_temp, bd=5);
        Get2.place(x=143, y=60)
        canvas.create_text(73, 120, text="车站名", font=("宋体", 10))
        Get3 = Entry(window_temp, bd=5);
        Get3.place(x=143, y=110)

        List_All=[]
        def back():
            window_temp.destroy()
            window = tk.Tk()
            choose2(window, self.Person1)
        def Get_s():
            List_Temp= self.Person1.Search_by_Station(Get2.get(), Get3.get())
            List_All.extend(List_Temp)
            List_Text=[]
            for i in range(len(List_All)):
                List_Text.append(Label(window_temp,text=str(List_All[i])))
                List_Text[i].grid(row=5+i,column=1)
            pass
        Button1=Button(window_temp,text='查询',command=Get_s, relief=GROOVE, bg='aliceblue');Button1.place(x=173,y=170)
        Button2 = Button(window_temp, text='返回', command=back, relief=GROOVE, bg='aliceblue');
        Button2.place(x=233, y=170)


    def back(self):
        self.window.destroy()
        window = tk.Tk()
        initWindow(window)


'''
    def Ticket_inquiry(self):
        Fu.

    def Train_management(self):
        Fu.

    def Station_inquiry(self):
        Fu.

    def Booking(self):
        Fu.

    def Return_a_ticket(self):
        Fu.
'''


def login():
    print("初始读取完成")
    print("车站数:", operator.length_hint(System.Stations.keys()) - 1, "车次数:",
          operator.length_hint(System.Trains.keys()) - 1)
    loginWindow = tk.Tk()  # 创建窗口
    LoginUi(loginWindow)  # 类初始化
    loginWindow.mainloop()  # 载入窗口循环
    print("close")
    exit(0)
login()
