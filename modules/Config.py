import os
import configparser
import json

CONFIG_FILE_NAME = r"./config/config.ini"

class SystemConfig(object):
    def __init__(self, parser):
        self.parser = parser

    def read(self):
        self._Version = self.parser.get("System", "Version")
        self._Path = self.parser.get("System", "Path")
        self._FlowDefine= self.parser.get("System", "FlowDefine")

    @property
    def Version(self):
        return self._Version

    @property
    def Path(self):
        return self._Path

    @property
    def FlowDefine(self):
        return self._FlowDefine


class WatchDogConfig(object):
    def __init__(self, parser):
        self.parser = parser

    def read(self):
        self._Interval = self.parser.get("WatchDog", "Interval")
        self._OverShoot = self.parser.get("WatchDog", "OverShoot")

    @property
    def Interval(self):
        return float(self._Interval)
    
    @property
    def OverShoot(self):
        return int(self._OverShoot)

class FlowDefineConfig(object):
    def __init__(self, parser):
        self.parser = parser
        self._hierarchy = dict()
    
    def read(self):
        self._FlowDefine= self.parser.get("System", "FlowDefine")
        with open(self._FlowDefine) as f:
            self._hierarchy = json.load(f)
    
    @property
    def Flow(self):
        return self._hierarchy
        

class Config(object):
    _instance = None

    def __init__(self, config_file):
        if not os.path.exists(config_file):
            raise FileNotFoundError(config_file)

        self.config_file = config_file
        self.parser = configparser.ConfigParser()

        self._System = SystemConfig(self.parser)
        self._WatchDog = WatchDogConfig(self.parser)
        self._FlowDefine = FlowDefineConfig(self.parser)

    @classmethod
    def getConfig(cls):
        if cls._instance is None:
            _instance = cls(CONFIG_FILE_NAME)
        return _instance

    def read(self):
        self.parser.read(self.config_file, "utf-8")

        self._System.read()
        self._WatchDog.read()
        self._FlowDefine.read()

    @property
    def System(self):
        return self._System

    @property
    def WatchDog(self):
        return self._WatchDog

    @property
    def FlowDefine(self):
        return self._FlowDefine
