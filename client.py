import socket

from server import PORT

EXIT = 'exit'


def _main():
    sock = socket.socket()
    sock.connect(('localhost', PORT))
    print('Соединение с сервером')

    while True:
        message = input('Введите сообщение:')
        if message == EXIT:
            break
        print(f'Отправка "{message}" серверу')
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print(f'Пришло "{data}" от сервера')
        print(data)

    sock.close()
    print('Соединение с сервером закрыто')


if __name__ == '__main__':
    _main()