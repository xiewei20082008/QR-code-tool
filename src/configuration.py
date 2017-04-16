# coding=utf8
import os
import json
import random
from toolkit import *
from os.path import join
import threading
import itertools


class Configuration:
    def random_interval(self):
        return random.uniform(self.data['scan_waittime_min'],
                              self.data['scan_waittime_max'])

    def _nextFilePath(self):
        folder = self.data['QRcode_path']
        for name in os.listdir(folder):
            f = os.path.join(folder, name)
            yield f

    def __init__(self):
        self.lock_nextFilePath = threading.Lock()
        rootPath = getRootPath()
        self.data = json.load(file(os.path.join(rootPath, "config.json")))
        print self.data['QRcode_path']

        if not os.path.exists(self.data['archieve_path']):
            os.makedirs(self.data['archieve_path'])

        self.gen_nextFilePath = self._nextFilePath()

    def getNextFilePath(self):
        self.lock_nextFilePath.acquire()
        try:
            v = self.gen_nextFilePath.next()
        except Exception:
            self.lock_nextFilePath.release()
            raise
        else:
            self.lock_nextFilePath.release()
            return v


if __name__ == '__main__':
    cfg = Configuration()
