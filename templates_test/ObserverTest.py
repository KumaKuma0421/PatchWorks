import os
import sys

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from templates.Observer import Observer, Subscriber


class MyObserver(Observer):
    def update(self, value):
        print("update({0}) called.".format(value))


class MySubscriber(Subscriber):
    pass

if __name__ == "__main__":
    observer = MyObserver()
    subscriber = MySubscriber()

    subscriber.attach(observer)
    subscriber.notify("One")
    subscriber.detach(observer)
    subscriber.notify("Nothing")
