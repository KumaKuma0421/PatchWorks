import os
import sys

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Config import Config

config = Config.getConfig()
config.read()

print("config.System.Version=" + config.System.Version)
print("config.System.Path=" + config.System.Path)
print("config.WatchDog.Interval={0}".format(config.WatchDog.Interval))
print("config.WatchDog.OverShoot={0}".format(config.WatchDog.OverShoot))