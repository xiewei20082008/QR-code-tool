from toolkit import *
import os
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
        print self.rootPath
        self.phonePath = '/storage/emulated/0/tencent/MicroMsg/WeiXin'
        self.env["PATH"] = os.path.join(
            self.rootPath, 'adb') + ";" + self.env["PATH"]

    def click(self, x, y):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' shell input tap ' + str(x) + ' ' + str(y)
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)

    def screenshot(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' exec-out screencap -p > ' + os.path.join(
            self.rootPath, 'cache', 'test.png')
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)

    def createDir(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' shell su -c "mkdir ' + self.phonePath + '"'
        print cmd
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
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)


op = adbOperator(20510497)
op.openScanner()
# op.pushPic('d:/microMsg.1491963504562.jpg')
