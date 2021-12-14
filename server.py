import socket
import threading
import shifrCezar

nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"  # "127.0.1.1"
port = 1212
my_socket.connect((host, port))


choise = str(input("Кодувати повідомлення?\n 'Yes'\n 'No'\n :"))


def thread_sending(selector, nickname):
    while True:
        message_to_send = input()
        if selector != "Yes":
                if message_to_send:
                    message_with_nickname = nickname.upper() + ":" + message_to_send.upper()
                    my_socket.send(message_with_nickname.encode())
                    print("Надіслано: " + message_with_nickname.lower())
                    my_socket.send(choise.encode())

        else:
                if message_to_send:
                    message_with_nickname = nickname.upper() + ":" + message_to_send.upper()
                    resilt = (shifrCezar.shifrrr(message_with_nickname))
                    my_socket.send(resilt.encode())
                    print("Надіслано з шифром: " + resilt.lower())
                    print("Надіслано без  шифра: " + message_with_nickname.lower())
                    my_socket.send(choise.encode())


def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        res = my_socket.recv(2048).decode()


thread_send = threading.Thread(target=thread_sending(choise, nickname))
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()