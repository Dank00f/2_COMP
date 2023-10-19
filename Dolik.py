import socket

while True:
    command = input('Введите ТЧ: ')
    if command == 'Терпкий':
        temp_image_path = r'C:\Users\Dankoff\PycharmProjects\pythonProject3\Barak.jpg'
        with open(temp_image_path, 'rb') as file:
            data = file.read()
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('ID', 53210))
        client_sock.sendall(data)
        client_sock.close()
    else:
        break