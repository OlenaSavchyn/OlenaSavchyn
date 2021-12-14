
import socket
import threading
import decode
import os

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 1212
ADDRESS = "0.0.0.0"
broadcast_list = []
my_socket.bind((ADDRESS, PORT))


def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listenning_thread(client)


def start_listenning_thread(client):
    client_thread = threading.Thread(
        target=listen_thread,
        args=(client,)  # список аргументів функції
    )
    client_thread.start()


def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        res = client.recv(2048).decode()
        if res == 'Yes':
            resultServer = (decode.shifrrr(message))
            print(f"Received message: {resultServer.lower()}")
        else:
            print(f"Received message: {message.lower()}")

def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")


accept_loop()