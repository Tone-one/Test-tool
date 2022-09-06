#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import *
# from androguard.core.bytecodes import apk
import os
from TestApp.main_interface.adb_run import Mothand

PATH = lambda p: os.path.abspath(p)
global label_img
global img_pngl

class Application(ttk.Frame):
    global label_img
    global img_pngl
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.init_window()

    def init_window(self):
        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        self.menu = tkinter.Menu(self.master)
        self.master.config(menu=self.menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        self.file = tkinter.Menu(self.menu)
        self.file.add_command(label='保存')
        self.file.add_command(label='退出')
        self.menu.add_cascade(label='File', menu=self.file)

        # 创建Edit菜单，下面有一个Undo菜单
        self.edit = tkinter.Menu(self.menu)
        self.edit.add_command(label='版本')
        self.edit.add_command(label='帮助')
        self.menu.add_cascade(label='Edit', menu=self.edit)

        ttk.Label(self.master, text="作者：可   时间：xx.xx.xx QQ：1191461802").grid(row=2, column=2)
        self.moudleAll()
    def moudleAll(self):
        self.tabControl = ttk.Notebook(self.master)
        self.fram_1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_1, text='安卓截屏')
        self.tabControl.grid(column=0, row=0, columnspan=2,padx=0)

        self.fram_2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_2, text='ADB')
        self.tabControl.grid(column=1, row=0)

        self.fram_3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_3, text='代码扫描')
        self.tabControl.grid(column=1, row=0)

        self.fram_4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_4, text='待扩展.....')
        self.tabControl.grid(column=1, row=0,padx=15)

        self.moudleOne()
    def moudleOne(self):

        self.frame_1 = ttk.LabelFrame(self.fram_1, text="= = = = = =截图显示区= = = = = =",labelanchor="n")
        self.frame_1.grid(column=1, row=1, pady=2,columnspan=1)

        self.moudleTwo()
    def moudleTwo(self):
        # ===================容器2======================
        self.frame_2 = ttk.LabelFrame(self.fram_2, text="ADB指令", labelanchor="n")
        self.frame_2.grid(column=0, row=0, pady=10,padx=10)

        self.frame_3 = ttk.LabelFrame(self.fram_2, text="APK安装", labelanchor="n")
        self.frame_3.grid(column=0, row=1, pady=10,padx=10)

        self.frame_4 = ttk.LabelFrame(self.fram_2, text="PC-ip", labelanchor="n")
        self.frame_4.grid(column=1, row=1, pady=10,padx=10)

        self.frame_5 = ttk.LabelFrame(self.fram_2, text="Android查询", labelanchor="n")
        self.frame_5.grid(column=1, row=0, pady=10,padx=10)
        # ===================容器3======================
        self.frame_6 = ttk.LabelFrame(self.fram_3, text="待定", labelanchor="n")
        self.frame_6.grid(column=0, row=0, pady=10,columnspan=2,padx=10)
        # ===================容器4======================
        self.frame_7 = ttk.LabelFrame(self.fram_4, text="待定", labelanchor="n")
        self.frame_7.grid(column=0, row=0, pady=10,columnspan=2,padx=15)

        # PNG初始图片设置
        global label_img
        global img_pngl

        img_png = PhotoImage(file='''png.png''')
        img_png = img_png.subsample(3, 3)
        # 容器一布局

        label_img = Label(self.frame_1,image=img_png,bg='#6495ED', height=650, width=380)
        label_img.grid(row=1, column=1, columnspan=2)

        ttk.Button(self.frame_1, text="查看图片").grid(row=2, column=1, pady=10)
        ttk.Button(self.frame_1, text="截图").grid(row=2, column=2, pady=10)


        # 底部菜单
        self.t = Text(self.frame_1 ,width=30, height=48)
        self.t.grid(row=1, column=3, columnspan=2,ipady=15,padx=60)

        ttk.Button(self.frame_1, text="获取Devices").grid(row=2, column=3)

        ttk.Button(self.frame_2,text="查看日志").grid(row=0, column=1,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="DeBug日志获取").grid(row=0, column=2,ipadx=25,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="长按操作（2h)").grid(row=1, column=1,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="ADB手机事件模拟").grid(row=1, column=2, ipadx=20,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="待扩展.....").grid(row=3, column=1, ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="待扩展.....",).grid(row=3, column=2, ipadx=30,pady=10,ipady=10,padx=30)

        ttk.Button(self.frame_3, text="批量安装目录下的APK包").grid(row=0, column=2, ipadx=10,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_3, text="查看目录下的安装包",command=Mothand._getFileInstall(self)).grid(row=0, column=1, ipadx=10,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_3, text="查看包名").grid(row=1, column=2,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_3, text="待扩展.....").grid(row=1, column=1,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_4, text="ping").grid(row=0, column=1, ipadx=15, padx=0)
        ttk.Button(self.frame_4, text="PC-IP").grid(row=0, column=2, ipadx=15, padx=0)

        ttk.Button(self.frame_5, text="查看安卓设备信息").grid(row=0, column=1, ipadx=15, padx=0)
        ttk.Button(self.frame_5, text="PC-IP").grid(row=0, column=2, ipadx=15, padx=0)

        self.moudleThree()
    def moudleThree(self):

        self.t2 = Text(self.frame_6 ,width=95, height=25)
        self.t2.grid(row=0, column=0, ipadx=15, padx=0,columnspan=2)
        ttk.Button(self.frame_6, text="文件关键字扫描").grid(row=1, column=1, ipadx=15,pady=5,ipady=10)
        ttk.Label(self.frame_6, text="关键字：aibei、wapPay、alipay、wechat、weixin、tenpay").grid(row=1, column=0, ipadx=15,pady=5,ipady=10)



root = tkinter.Tk()
root.title("TestQa")
root.geometry("750x800")

#root.resizable(width=False, height=False)
app = Application(root)
root.mainloop()