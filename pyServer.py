#!/usr/bin/env python3
import socket
import threading

PORT = 8000
ADDRESS = "0.0.0.0"

broadcast_list = []
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((ADDRESS, PORT))

#Allow connections
def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listening_thread(client)
        print("Client joined the server")
        
def start_listening_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,)
        )
    client_thread.start()
    
def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            print(message)
            broadcast(message)
        else:
            print(f"{client} has disconnected")
            return
        
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client was removed from the server")
accept_loop()
