# coding=utf8
from toolkit import *
import shutil
import os
from time import sleep
import sys
import threading
import subprocess32 as subprocess
import configuration
from subprocess32 import PIPE
from os.path import dirname


class adbOperator:
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.env = os.environ.copy()
        # print self.env["PATH"]
        self.rootPath = getRootPath()
        self.phonePath = '/storage/emulated/0/Pictures/Screenshots'
        self.env["PATH"] = os.path.join(
            self.rootPath, 'adb') + ";" + self.env["PATH"]

    def click(self, x, y):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' shell input tap ' + str(x) + ' ' + str(y)
        p = subprocess.Popen(cmd, stderr=PIPE, env=self.env, shell=True)
        try:
            waitSubprocess(p)
        except "suberr":
            raise

    def screenshot(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' exec-out screencap -p > ' + os.path.join(
            self.rootPath, 'cache', 'test.png')
        p = subprocess.Popen(cmd, stderr=PIPE, env=self.env, shell=True)
        try:
            waitSubprocess(p)
        except "suberr":
            raise

    def createDir(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' shell su -c "mkdir ' + self.phonePath + '"'
        p = subprocess.Popen(cmd, stderr=PIPE, env=self.env, shell=True)
        try:
            waitSubprocess(p)
        except "suberr":
            raise

    def openScanner(self):
        cmd = 'adb -s ' + str(self.deviceId) + \
            (' shell su -c "am start -n com.tencent.mm/'
             'com.tencent.mm.plugin.scanner.ui.BaseScanUI"')
        print cmd
        p = subprocess.Popen(cmd, stderr=PIPE, env=self.env, shell=True)
        try:
            waitSubprocess(p)
        except "suberr":
            raise

    def pushPic(self, picFile):
        cmd = 'adb -s ' + str(self.deviceId) + \
            ' push ' + picFile + ' ' + self.phonePath
        p = subprocess.Popen(cmd, stderr=PIPE, env=self.env, shell=True)
        try:
            waitSubprocess(p)
        except "suberr":
            raise

        cmd = 'adb -s ' + str(self.deviceId) + \
            (' shell am broadcast -a '
             'android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://') + \
            self.phonePath + '/' + os.path.basename(picFile)
        print cmd
        p = subprocess.Popen(cmd, stderr=PIPE, env=self.env, shell=True)
        try:
            waitSubprocess(p)
        except "suberr":
            raise

    def scanQR(self, picFile):
        try:
            self.pushPic(picFile)
            sleep(1.0)
            self.openScanner()
            sleep(5.0)
            self.click(674, 93)  # 点三个点
            sleep(2.0)
            self.click(477, 293)  # 点本地图片
            sleep(5.0)
            self.click(353, 289)  # 点图片缩略图
        except "suberr":
            raise


def deviceThread(deviceId, cfg):
    while True:
        print '%s start scan' % deviceId
        op = adbOperator(deviceId)
        try:
            f = cfg.getNextFilePath()
            print f
        except StopIteration:
            print 'end thread'
            break
        try:
            op.scanQR(f)
        except SubErr as e:
            print 'scan error in subprocess!'
        else:
            dst = os.path.join(cfg.data['archieve_path'], os.path.basename(f))
            print dst
            shutil.move(f, dst)

        interval = cfg.random_interval()
        print 'interval is'
        print interval
        sleep(interval)


def scanAllFiles():
    cfg = configuration.Configuration()

    for i in cfg.data['deviceIds']:
        t = threading.Thread(target=deviceThread, args=(i, cfg))
        t.start()
    # sleep(100)


# op = adbOperator(20510497)
# try:
#     op.openScanner()
# except SubErr as e:
#     print e
# op.scanQR('d:/1.jpg')
scanAllFiles()
