# Python3.x 导入方法
from tkinter import * 
import tkinter.messagebox
import os
import  tkinter.font   as  tkFont  #导入Tkinter字体模块
# def login():
# 	text.delete(0.0,END)
# 	text.insert(0.0,"登录成功!")

#to_list：
#1、 手动点击保存
#2、

#乱码的话改一下变成gbk
def save():
    print("save:",dataList)
    with open("database.txt",'w',encoding='utf-8') as f:
        for data in dataList:
            if len(data)==0:
                continue
            if(data[-1]!='\n'):
                f.writelines(data+'\n')
            else:
                f.writelines(data)
def read():
    with open('database.txt','r',encoding='utf-8') as f :
        temp = f.readlines()
        for x in temp :
            dataList.append(x)
def exit_tkinter():
    # tkinter.messagebox.showwarning(title='警告', message='刚才你点击了关闭按钮')
    v = tkinter.messagebox.askokcancel(title='退出',message="确认退出？ 您的文档将自动保存 请勿删除该目录下的txt文件")
    if v:
        save()
        root.destroy()
        os._exit(0)
def insertDatabase():#实际上异步插入
    print(text.get("1.0",END))
    insert_string=text.get("1.0",END)
    if insert_string not in dataList:
        dataList.append(insert_string)
def search():
    # search_list=[]
    del search_list[:]
    opString = text.get("1.0",END)
    opString = opString[:-1]
    print(len(opString))
    listb.delete(0, "end")
    print("dataList: ",dataList)
    print("opstring: ",opString)
    for x in dataList:
        if opString in x:
            print("111")
            search_list.append(x)
            listb.insert(0,x)
insert_string = ""
search_list = []
dataList = []
read()
opString=""
root = Tk()                     # 创建窗口对象的背景色                   # 创建两个列表
root.geometry("1300x900") 
root.title("文献检索工具")
# l = Label(root,width=20,height=2,text="输入")
# l.pack()
# text = Text(root, width=50, height=50)
# text.pack()
# text.insert("insert", "林四儿")  # 插入光标当前位置
# text.insert("end", "最帅")  # 插入末尾位置
li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root,width=123)          #  创建两个列表组件
# listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
    # listb.delete(0, "end")

# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
listb.grid(row=2,column=1) 
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()

GetData_button = Button(root,text="查找文献",command=search)
GetData_button.grid(row=10,column=10,sticky=E) 
helv15 = tkFont.Font ( family="黑体",size=15)
text = Text(root, width=12, height=10,font = helv15)
text.grid(row=20,column=10)
# text.grid(row=10,column=10)
InsertData_button = Button(root,text="插入",command=insertDatabase)
InsertData_button.grid(row=12,column=12,sticky=E) 

# L1 = Label(root, text="用户名：")
# L1.grid(row=0,column=0,sticky=W)
# E1 = Entry(root, bd =5)
# E1.grid(row=0,column=1,sticky=E)
# L2 = Label(root, text="密码：")
# L2.grid(row=1,column=0,sticky=W)
# E2 = Entry(root, bd =5,show='*')
# E2.grid(row=1,column=1,sticky=E) 
# B = Button(root,text="登 录",command=login)
# B.grid(row=2,column=1,sticky=E) 
# text = Text(root, width=20, height=1)
# text.place(x=15,y=65)
root.protocol("WM_DELETE_WINDOW", exit_tkinter)
root.mainloop()                 # 进入消息循环




