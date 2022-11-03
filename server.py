import socket

PORT = 2121


def _main():
    sock = socket.socket()
    sock.bind(('', PORT))
    print('Запуск сервера')
    sock.listen()
    print('Прослушивания порта:', PORT)
    conn, addr = sock.accept()
    print('Подключение клиента:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        decoded = data.decode()
        print(f'Пришло "{decoded}" от клиента', addr)
        conn.send(data)
        print(f'Отправка "{decoded}" клиенту', addr)

    conn.close()
    print('Отключение клиента', addr)
    sock.close()
    print('Отключение сервера')


if __name__ == '__main__':
    _main()