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
        subprocess.Popen(cmd, env=self.env, shell=True)

    def pushPic(self, picFile):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' push ' + picFile + ' ' + self.phonePath
        subprocess.Popen(cmd, env=self.env, shell=True)

        cmd = 'adb -s ' + str(self.deviceId) + \
            (' shell am broadcast -a '
             'android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://') + \
            os.path.join(self.phonePath + os.path.basename(picFile))
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)


op = adbOperator(20510497)
# op.openScanner()
op.pushPic('d:/1.jpg')
