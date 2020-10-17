#
# sample from https://www.sejuku.net/blog/23149
#

import logging.config


class Logger(logging.LoggerAdapter):

    def __init__(self, handler=''):
        logging.config.fileConfig(r'.\config\logging.ini')
        self.logger = logging.getLogger(handler)

    @classmethod
    def getLogger(cls, handler=''):
        return cls(handler).logger
