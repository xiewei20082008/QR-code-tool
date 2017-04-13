# coding=utf8
import os
import json
from toolkit import *
from os.path import join
import itertools


class Configuration:
    def __init__(self):
        rootPath = getRootPath()
        self.data = json.load(file(os.path.join(rootPath, "config.json")))
        print self.data['QRcode_path']

        if not os.path.exists(self.data['archieve_path']):
            os.makedirs(self.data['archieve_path'])

        self.gen_deviceIds = itertools.cycle(self.data['deviceIds'])

if __name__ == '__main__':
    cfg = Configuration()
