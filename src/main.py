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
        self.rootPath = dirname(dirname(__file__))
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
            self.rootPath,'cache', 'test.png')
        print cmd
        subprocess.Popen(cmd, env=self.env, shell=True)


op = adbOperator(1661505619)
op.screenshot()
