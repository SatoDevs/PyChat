#!/usr/bin/env python3
import socket
import threading
import pyfiglet
from termcolor import colored

host = "localhost"
port = 8000

print(pyfiglet.figlet_format('PyChat', font='big'))

nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname can't be empty : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((host, port))

def thread_sending():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())
        
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
