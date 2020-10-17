import configparser


class SystemConfig(object):
    def __init__(self, parser):
        self.parser = parser

    def read(self):
        self._os = self.parser.get("System", "os")
        self._version = self.parser.get("System", "version")
        self._path = self.parser.get("System", "path")

    @property
    def os(self):
        return self._os

    @property
    def version(self):
        return self._version

    @property
    def path(self):
        return self._path


class ClockGeneratorConfig(object):
    def __init__(self, parser):
        self.parser = parser

    def read(self):
        self._interval = self.parser.get("ClockGenerator", "interval")

    @property
    def interval(self):
        return float(self._interval)


class Config(object):
    _instance = None

    def __init__(self, config_file):
        self.config_file = config_file
        self.parser = configparser.ConfigParser()

        self._System = SystemConfig(self.parser)
        self._ClockGenerator = ClockGeneratorConfig(self.parser)

    @classmethod
    def getConfig(cls):
        if cls._instance is None:
            _instance = cls(r".\config\config.ini")
        return _instance

    def read(self):
        self.parser.read(self.config_file, "utf-8")

        self._System.read()
        self._ClockGenerator.read()

    @property
    def System(self):
        return self._System

    @property
    def ClockGenerator(self):
        return self._ClockGenerator
