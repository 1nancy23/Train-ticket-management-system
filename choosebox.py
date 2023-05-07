import tkinter as tk
#f
from tkinter import Checkbutton,Button
win = tk.Tk()
# win.title('按钮测试')
# win.geometry('300x300')
#
#
# def handler(num):
#     print("传过来的数字是：", num)
#
#
# for i in range(5):
#     btn = tk.Button(win, text="按钮" + str(i), command=lambda num=i: handler(num))
#     btn.pack()
# win.mainloop()
# i = 99
List_Int=[tk.BooleanVar() for _ in range(5)]
print([id(i) for i in List_Int])
Checkbutton1=Checkbutton(win,text="A",variable=List_Int[0])
Checkbutton1.grid(row=1,column=1)
Checkbutton2 = Checkbutton(win, text="B",variable=List_Int[1])
Checkbutton2.grid(row=1, column=2)
Checkbutton3 = Checkbutton(win, text="C",variable=List_Int[2])
Checkbutton3.grid(row=2, column=1)
Checkbutton4 = Checkbutton(win, text="D",variable=List_Int[3])
Checkbutton4.grid(row=2, column=2)
Checkbutton5=Checkbutton(win,text='E',variable=List_Int[4])
Checkbutton5.grid(row=3,column=1)


def Chcek():
    print([x.get() for x in List_Int])



Button1 = Button(win, text='确定', command=Chcek);
Button1.grid(row=3, column=2)
win.mainloop()