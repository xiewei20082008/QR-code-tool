# coding=utf8
import os
import json
import random
from toolkit import *
from os.path import join
import itertools


class Configuration:
    def _random_interval(self):
        while True:
            yield random.uniform(self.data['scan_waittime_min'],
                                 self.data['scan_waittime_max'])

    def __init__(self):
        rootPath = getRootPath()
        self.data = json.load(file(os.path.join(rootPath, "config.json")))
        print self.data['QRcode_path']

        if not os.path.exists(self.data['archieve_path']):
            os.makedirs(self.data['archieve_path'])

        self.gen_deviceIds = itertools.cycle(self.data['deviceIds'])
        self.gen_random_interval = self._random_interval()


if __name__ == '__main__':
    cfg = Configuration()
