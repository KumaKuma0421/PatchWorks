import os
import sys
import threading
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Logger import Logger

def root_test():
    logger = Logger.getLogger()
    logger.critical("root critical")
    logger.error("root error")
    logger.warning("root warning")
    logger.info("root info")
    logger.debug("root debug")
    logger.log(0, "root notset")


def stream_test():
    logger = Logger.getLogger("Stream")
    logger.critical("Stream critical")
    logger.error("Stream error")
    logger.warning("Stream warning")
    logger.info("Stream info")
    logger.debug("Stream debug")
    logger.log(0, "Stream notset")


def file_test():
    logger = Logger.getLogger("File")
    logger.critical("File critical")
    logger.error("File error")
    logger.warning("File warning")
    logger.info("File info")
    logger.debug("File debug")
    logger.log(0, "File notset")

def rotation_file_test():
    logger = Logger.getLogger("RotatingFile")
    logger.critical("RotatingFile critical")
    logger.error("RotatingFile error")
    logger.warning("RotatingFile warning")
    logger.info("RotatingFile info")
    logger.debug("RotatingFile debug")
    logger.log(0, "RotatingFile notset")

logger = Logger.getLogger("RotatingFile")

def multi_thread_test():
    for i in range(100):
        logger.critical("RotatingFile critical {0}".format(i))
        time.sleep(0)
        logger.error("RotatingFile error {0}".format(i))
        time.sleep(0)
        logger.warning("RotatingFile warning {0}".format(i))
        time.sleep(0)
        logger.info("RotatingFile info {0}".format(i))
        time.sleep(0)
        logger.debug("RotatingFile debug {0}".format(i))
        time.sleep(0)
        logger.log(0, "RotatingFile notset {0}".format(i))
        time.sleep(0)

if __name__ == "__main__":
    root_test()
    stream_test()
    file_test()
    rotation_file_test()
    
    threading.Thread(target=multi_thread_test).start()
    threading.Thread(target=multi_thread_test).start()
    threading.Thread(target=multi_thread_test).start()
    threading.Thread(target=multi_thread_test).start()