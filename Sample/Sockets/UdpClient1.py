#
# UDP送信
# sa https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
#
import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP', (HOST, PORT))
