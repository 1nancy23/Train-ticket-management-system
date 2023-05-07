from tkinter import *
import tkinter as tk
import tkinter
class Change_Tickt():
    def __init__(self,Person,window_expread,row,column):
        self.Person=Person
        self.Button1=Button(window_expread,text='改签',command=self.Get_Old_Information)
        self.Button1.place(x=row,y=column)
    def Get_Old_Information(self):
        print(1)
        window_temp_1 = tk.Tk()
        Label1=Label(window_temp_1,text='请输入退票人身份证')
        Label1.grid(row=1,column=1)
        Get1=Entry(window_temp_1)
        Get1.grid(row=1,column=1)
        List_temp=[]
        def Serach_():
            All_Information=self.Person.Return_tickts(Get1.get())
            print(2)
            def change(i):
                Old_Information=All_Information[i]
                Station_begin,Station_end=Old_Information[1],Old_Information[2]
                Get2=Entry(window_temp_1,textvariable="请输入想要改签的日期")
                Get2.grid(row=2,column=2)
                New_All=self.Person.Search_by_DAY(Get2.get(),Station_begin,Station_end)
                window_temp2=tk.Tk()
                labels=[]
                def check_sure(x):
                    self.Person.Back_Tickt(Get1.get(),Old_Information[0])
                    self.Person.Buy_Tickt(Get1.get(),New_All[i][0],New_All[x][1],New_All[x][2],New_All[x][3],[0,0],New_All[x][4])
                    tkinter.messagebox.showinfo('改签', '改签成功')
                for c in range(len(New_All)):
                    labels.append(Button(window_temp2,text=str(New_All[c]),command=(lambda num: lambda: check_sure(num))(c)))
                    labels[c].grid(row=c,column=1)
            for i in range(len(All_Information)):
                List_temp.append(Button(window_temp_1,text=str(All_Information[i]),command=(lambda num: lambda: change(num))(i)))
                List_temp[i].grid(row=i,column=1)
        Button1=Button(window_temp_1,text='确定',command=Serach_)
        Button1.grid(row=2,column=1)
