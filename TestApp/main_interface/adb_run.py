#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from tkinter import filedialog
from tkinter import *
import time
import _thread


PATH = lambda p: os.path.abspath(p)

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
#   def svnLog(self):
#        subprocess.Popen(r'TortoiseProc.exe /command:update /path:"E:\SVnwc\策划文档" /closeonend:0')

    def apkInstall(self):
        filepath = PATH(os.getcwd() + "/testApk")
        # filepath = self.install_getFile()
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
    # 获取APK包
    def install_getFile(self):
        filepath = PATH(os.getcwd())
        self.filePath = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(filepath)))
        self.printSomeWords(self.filePath)
        filepathv=self.printSomeWords(self.filePath)
        return filepathv
    # 获取pc地址
    def get_ip(self):
        self.tempopen = os.popen("ipconfig")
        self.androiddevice = self.tempopen.read()
        self.printSomeWords(self.androiddevice)

    # ping
    def get_Ping(self):
        self.tempopen = os.popen(r"ping www.baidu.com")
        self.get_ping = self.tempopen.read()
        return self.printSomeWords(self.get_ping)

    # 获取log
    def get_log(self):
        filepath = PATH(os.getcwd() + "/Log")
        self.filePath = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(filepath)))
        #self.androiddevice = getlog.read()
        #self.printSomeWords(self.androiddevice)
    def set_log(self):
        filepath = PATH(os.getcwd() + "/Log"+"/log.txt")
        os.popen('adb logcat -v time > %s' %(filepath))
        self.printSomeWords(filepath)
    # 代码扫描
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
    # 扫描执行入口
    def _sMain(self):
        #filepath = PATH(os.getcwd() + "/testApk")
        #self.printSomeWords_1(filepath)
        list_a = ["aibei", "wapPay","alipay", "wechat","weixin", "tenpay"]
        for self.fn in list_a:
            self.printSomeWords_1("扫描关键字： %s " % (self.fn))
            self.walkFiles("E:\\工作目录\\v2_\\dist\\ui_2\\testApk", "%s" % (self.fn))
            self.printSomeWords_1("扫描关键字完成： %s \n" % (self.fn))

    def get_Android(self):

        self.brand = os.popen("adb -d shell getprop ro.product.brand")
        self.brand_1 =self.brand.read()
        self.printSomeWords("厂商: %s"%(self.brand_1))

        self.model = os.popen("adb -d shell getprop ro.product.model")
        self.model_1 =self.model.read()
        self.printSomeWords("设备型号: %s"%(self.model_1))

        self.release = os.popen("adb shell getprop ro.build.version.release")
        self.release =self.release.read()
        self.printSomeWords("系统版本: %s"%(self.release))

        self.size = os.popen("adb shell wm size")
        self.size_1 =self.size.read()
        self.printSomeWords("手机分辨率: %s"%(self.size_1))