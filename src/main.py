#coding=utf8
from toolkit import *
import os
from time import sleep
import sys
import subprocess
from os.path import dirname


class adbOperator:
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.dm = reg()
        self.env = os.environ.copy()
        # print self.env["PATH"]
        self.rootPath = os.path.abspath('..')
        self.phonePath = '/storage/emulated/0/tencent/MicroMsg/WeiXin'
        self.env["PATH"] = os.path.join(
            self.rootPath, 'adb') + ";" + self.env["PATH"]

    def click(self, x, y):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' shell input tap ' + str(x) + ' ' + str(y)
        subprocess.Popen(cmd, env=self.env, shell=True)

    def screenshot(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' exec-out screencap -p > ' + os.path.join(
            self.rootPath, 'cache', 'test.png')
        subprocess.Popen(cmd, env=self.env, shell=True)

    def createDir(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' shell su -c "mkdir ' + self.phonePath + '"'
        subprocess.Popen(cmd, env=self.env, shell=True)

    def openScanner(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            (' shell su -c "am start -n com.tencent.mm/'
             'com.tencent.mm.plugin.scanner.ui.BaseScanUI"')
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)

    def pushPic(self, picFile):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' push ' + picFile + ' ' + self.phonePath
        subprocess.Popen(cmd, env=self.env, shell=True)

        cmd = 'adb -s ' + str(self.deviceId) + \
            (' shell am broadcast -a '
             'android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://') + \
            self.phonePath+'/'+os.path.basename(picFile)
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)

    def scanQR(self,picFile):
        self.pushPic(picFile)
        sleep(1.0)
        self.openScanner()
        sleep(5.0)
        self.click(674,93) #点三个点
        sleep(2.0)
        self.click(477,293) # 点本地图片
        sleep(5.0)
        self.click(353,289) # 点图片缩略图


op = adbOperator(20510497)
# op.openScanner()
op.scanQR('d:/1.jpg')
