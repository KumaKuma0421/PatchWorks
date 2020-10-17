import os
import sys

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Config import Config

config = Config.getConfig()
config.read()

print("config.System.os=" + config.System.os)
print("config.System.version=" + config.System.version)
print("config.System.path=" + config.System.path)
print("config.ClockGenerator.interval={0}".format(config.ClockGenerator.interval))