#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk, filedialog
from tkinter import *   # 导入画布容器
from androguard.core.bytecodes import apk
import os
import _thread
import time

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
        self.path_fold_show = tkinter.StringVar()
        self.mothand =Mothand
        self.cheakAppInfo = CheakAppInfo
        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        self.menu = tkinter.Menu(self.master)
        self.master.config(menu=self.menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        self.file = tkinter.Menu(self.menu)
        self.file.add_command(label='保存')
        self.file.add_command(label='退出',command=self.mothand.client_exit)
        self.menu.add_cascade(label='File', menu=self.file)

        # 创建Edit菜单，下面有一个Undo菜单
        self.edit = tkinter.Menu(self.menu)
        self.edit.add_command(label='版本')
        self.edit.add_command(label='帮助')
        self.menu.add_cascade(label='Edit', menu=self.edit)
        # 底部菜单
        self.t = Text(self.master ,width=90, height=5)
        self.t.grid(row=2, column=1, columnspan=2,ipady=15)
        ttk.Button(self.master, text="获取Devices",command=self.mothand(self.t).getDevices).grid(row=3, column=1)
        ttk.Label(self.master, text="作者：可   时间：xx.xx.xx QQ：1191461802").grid(row=4, column=1)

        # 4容器菜单栏
        self.tabControl = ttk.Notebook(self.master)
        self.fram_1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_1, text='安卓截屏')
        self.tabControl.grid(column=0, row=0, padx=0)

        self.fram_2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_2, text='ADB')
        self.tabControl.grid(column=1, row=0)

        self.fram_3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_3, text='代码扫描')
        self.tabControl.grid(column=1, row=0)

        self.fram_4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.fram_4, text='待扩展..')
        self.tabControl.grid(column=1, row=0,padx=15)
        # ==4容器布局===
        # ===================容器1======================
        self.frame_1 = ttk.LabelFrame(self.fram_1, text="= = = = = =截图 = = = = = =",labelanchor="n")
        self.frame_1.grid(column=0, row=0, pady=10,columnspan=2,padx=0)

        # ===================容器2======================
        self.frame_2 = ttk.LabelFrame(self.fram_2, text="ADB指令", labelanchor="n")
        self.frame_2.grid(column=0, row=0, pady=10,padx=10)

        self.frame_3 = ttk.LabelFrame(self.fram_2, text="APK安装", labelanchor="n")
        self.frame_3.grid(column=0, row=1, pady=10,padx=10)

        self.frame_4 = ttk.LabelFrame(self.fram_2, text="PC-ip", labelanchor="n")
        self.frame_4.grid(column=1, row=1, pady=10,padx=10)

        self.frame_5 = ttk.LabelFrame(self.fram_2, text="APK信息", labelanchor="n")
        self.frame_5.grid(column=1, row=0, pady=10,padx=10)
        # ===================容器3======================
        self.frame_6 = ttk.LabelFrame(self.fram_3, text="= = = = = =扫描结果 = = = = = =", labelanchor="n")
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

        label_img = Label(self.frame_1,image=img_png,bg='#6495ED', height=380, width=720)
        label_img.grid(row=0, column=1, columnspan=2)

        ttk.Button(self.frame_1, text="查看图片",command = self.mothand(self.t)._getFile).grid(row=2, column=1, pady=10)
        ttk.Button(self.frame_1, text="截图",command = self.mothand(self.t).throwThreadgetCapture).grid(row=2, column=2, pady=10)

        ttk.Button(self.frame_2,text="查看日志",command=self.mothand(self.t).get_log).grid(row=0, column=1,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="DeBug日志获取",command=self.mothand(self.t).set_log).grid(row=0, column=2,ipadx=25,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="长按操作（2h)",command=self.mothand(self.t).onlyUp).grid(row=1, column=1,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="ADB手机事件模拟",command=self.mothand(self.t).onlymn).grid(row=1, column=2, ipadx=20,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="待扩展..").grid(row=3, column=1, ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_2, text="待扩展..",).grid(row=3, column=2, ipadx=30,pady=10,ipady=10,padx=30)


        ttk.Button(self.frame_3, text="批量安装目录下的APK包", command=self.mothand(self.t).apkInstall).grid(row=0, column=2, ipadx=10,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_3, text="查看目录下的安装包",command = self.mothand(self.t)._getFileInstall).grid(row=0, column=1, ipadx=10,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_3, text="查看包名",command = self.cheakAppInfo(self.t).AnalyzePackage).grid(row=1, column=2,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_3, text="待扩展..").grid(row=1, column=1,ipadx=30,pady=10,ipady=10,padx=30)
        ttk.Button(self.frame_4, text="ping",command = self.mothand(self.t).get_Ping).grid(row=0, column=1, ipadx=15, padx=0)
        ttk.Button(self.frame_4, text="PC-IP",command = self.mothand(self.t).get_ip).grid(row=0, column=2, ipadx=15, padx=0)

        ttk.Button(self.frame_5, text="ping",command = self.mothand(self.t).get_Ping).grid(row=0, column=1, ipadx=15, padx=0)
        ttk.Button(self.frame_5, text="PC-IP",command = self.mothand(self.t).get_ip).grid(row=0, column=2, ipadx=15, padx=0)

        #容器3

        self.t2 = Text(self.frame_6 ,width=95, height=25)
        self.t2.grid(row=0, column=0, ipadx=15, padx=0,columnspan=2)
        ttk.Button(self.frame_6, text="文件关键字扫描",command=self.mothand(self.t2)._sMain).grid(row=1, column=1, ipadx=15,pady=5,ipady=10)
        ttk.Label(self.frame_6, text="关键字：aibei、wapPay、alipay、wechat、weixin、tenpay").grid(row=1, column=0, ipadx=15,pady=5,ipady=10)

class Mothand:

    def __init__(self,t):
        self.t = t

    def client_exit(self):
        exit()

    # 公共输出框，暂时公共信息
    def printSomeWords(self,inputString):
        self.inputString = inputString
        self.t.insert(END,self.inputString + '\n')
        self.t.see(END)

    # 展示扫描结果
    def printSomeWords_1(self,inputString):
        self.inputString = inputString
        self.t.insert(END,self.inputString + '\n')
        self.t.see(END)

    # 读取devices数据
    def getDevices(self):
        self.printSomeWords("获取Devices")
        self.deviceInfo = self.androidDevice()
        self.printSomeWords(str(self.deviceInfo))

    # 操作devices
    def androidDevice(self):
        self.tempopen = os.popen("adb devices")
        self.androiddevice = self.tempopen.read()
        return self.androiddevice

    def throwThreadgetCapture(self):
        # 创建两个线程
        try:
            _thread.start_new_thread(self.getCapture,())
        except:
            print("Error: 无法启动线程")

    def getCapture(self):
        print("getCapture START")
        self.printSomeWords("截图中请等待刷新")
        self.tempImage = self.screenshot()
        self.printSomeWords("getImageName is " + self.tempImage)
        time.sleep(2.5)
        return self.showAimage(self.tempImage)

    def showAimage(self,filename):
        pass
        global label_img
        global img_pngl
        img_pngl = PhotoImage(file=str(filename))

        img_pngl = img_pngl.subsample(3, 3)
        # 获取图像的原始大小

        label_img.configure(image=img_pngl)
    def screenshot(self):
        path = PATH(os.getcwd() + "/screenshot")

        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        # os.popen("adb wait-for-device")
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
            os.makedirs(path)

        time.sleep(3.5)
        tempopen = os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))

        print(tempopen)
        # time.sleep(2)
        os.popen("adb shell rm /data/local/tmp/tmp.png")
        print("success")
        return PATH(path + "/" + timestamp + ".png")

    def onlyUp(self):
        stringSwipe = "adb shell input swipe 500 500 100 100 7200000 "#2小时
        os.popen(stringSwipe)
        self.printSomeWords("长按操作——————————————————————————————————")
    def onlymn(self):
        stringSwipe = "adb shell monkey -p com.yxby10110.huntfish.nearme.gamecenter --kill-process-after-error -v -v -v 1000000 "#2小时
        os.popen(stringSwipe)
        self.printSomeWords("ADB手机事件模拟触发成功")

    def apkInstall(self):
        filepath = PATH(os.getcwd() + "/testApk")
        #filepath = self.install_getFile()
        files = os.listdir(filepath)
        a = 0
        for file in files:
            if file.endswith('.apk'):
                os.popen('adb install %s\\\\"%s\"'%(filepath,file))
                time.sleep(5)

                a += 1
            else:
                continue

        self.printSomeWords('\n总共安装了{}个APK\n'.format(a))
    # 查看图片
    def _getFile(self):
        filepath = PATH(os.getcwd() + "/screenshot")

        self.filePath = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(filepath)))
        self.printSomeWords(self.filePath)
    # 查看目录安装包
    def _getFileInstall(self):
        filepath = PATH(os.getcwd() + "/testApk")
        self.filePath = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(filepath)))
        self.printSomeWords(self.filePath)
    #获取APK包
    def install_getFile(self):
        filepath = PATH(os.getcwd())
        self.filePath = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(filepath)))
        self.printSomeWords(self.filePath)
        filepathv=self.printSomeWords(self.filePath)
        return filepathv
    #获取pc地址
    def get_ip(self):
        self.tempopen = os.popen("ipconfig")
        self.androiddevice = self.tempopen.read()
        self.printSomeWords(self.androiddevice)

    #ping
    def get_Ping(self):
        self.tempopen = os.popen(r"ping www.baidu.com")
        self.get_ping = self.tempopen.read()
        return self.printSomeWords(self.get_ping)

    #获取log
    def get_log(self):
        filepath = PATH(os.getcwd() + "/Log")
        self.filePath = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(filepath)))

    def set_log(self):
        filepath = PATH(os.getcwd() + "/Log"+"/log.txt")
        os.popen('adb logcat -v time > %s' %(filepath))
        self.printSomeWords(filepath)
    #代码扫描
    def walkFiles(self,root, string):
        self.root=root
        self.string=string
        s = os.sep
        for dirpath, dirname, filename in os.walk(self.root):
            for fn in filename:
                try:
                    name = dirpath + s + fn
                    # print("Searcing file '" + name + "'...")
                    flag = 0
                    fp = open(name, 'r')
                    count = 0
                    for line in fp.readlines():
                        count += 1
                        if self.string in line:
                            flag = 1
                            self.printSomeWords_1("Your string is in file '" + name + "' line " + str(count))
                    if flag == 0:
                        pass
                except:
                    pass
    #扫描执行入口
    def _sMain(self):

        list_a = ["weixin", "aibei","wapPay", "wechat","tenpat", "alipat","weChat"]
        for self.fn in list_a:
            self.printSomeWords_1("扫描关键字： %s " % (self.fn))
            self.walkFiles("E:\\工作目录\\v2_\\dist\\ui_2\\testApk", "%s" % (self.fn))
            self.printSomeWords_1("扫描关键字完成： %s \n" % (self.fn))

class CheakAppInfo:
    def __init__(self, t):
        self.t = t

    def AnalyzePackage(self):

        filepath = PATH(os.getcwd() + "/package")
        files = os.listdir(filepath)

        for file in files:
            if not file.endswith("apk"):
                self.printSomeWords("没包你查啥~")
            else:
                self.package_file = ("%s\%s" %(filepath,file))
                self.apkInfo = apk.APK(self.package_file)

        app_name = self.apkInfo.get_app_name()
        package = self.apkInfo.get_package()
        androidversion_name = self.apkInfo.get_androidversion_name()
        androidversion_code = self.apkInfo.get_androidversion_code()
        main_activity = self.apkInfo.get_main_activity()

        self.printSomeWords("app名称：%s"%str(app_name))
        self.printSomeWords("package：%s"%str(package))
        self.printSomeWords("androidversion_name：%s"%str(androidversion_name))
        self.printSomeWords("androidversion_code：%s"%str(androidversion_code))
        self.printSomeWords("main_activity：%s"%str(main_activity))

    def printSomeWords(self,inputString):
        self.inputString = inputString
        self.t.insert(END,self.inputString + '\n')# Extry 不能接受消息，可以用Text
        self.t.see(END)

root = tkinter.Tk()
root.title("TestQa")
root.geometry("760x650")

root.resizable(width=False, height=False)
app = Application(root)
root.mainloop()
