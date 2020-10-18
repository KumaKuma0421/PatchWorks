#
# sample from https://www.sejuku.net/blog/23149
#

import logging.config
from modules.Config import Config

class Logger(logging.LoggerAdapter):

    def __init__(self, handler=''):
        config = Config.getConfig()
        config.read()
        logging_file = config.System.Logging
        logging.config.fileConfig(logging_file)
        self.logger = logging.getLogger(handler)

    @classmethod
    def getLogger(cls, handler=''):
        return cls(handler).logger
