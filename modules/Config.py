import configparser
import json

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


class Config(object):
    _instance = None

    def __init__(self, config_file):
        self.config_file = config_file
        self.parser = configparser.ConfigParser()

        self._System = SystemConfig(self.parser)
        self._WatchDog = WatchDogConfig(self.parser)

    @classmethod
    def getConfig(cls):
        if cls._instance is None:
            _instance = cls(r".\config\config.ini")
        return _instance

    def read(self):
        self.parser.read(self.config_file, "utf-8")

        self._System.read()
        self._WatchDog.read()

    @property
    def System(self):
        return self._System

    @property
    def WatchDog(self):
        return self._WatchDog
