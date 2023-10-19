import socket
import sys
import io
from PyQt5 import QtWidgets
from PIL import Image

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('ID', 53210))
serv_sock.listen(10)
count = 0

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        self.data = data

        super(MainWindow, self).__init__()
        self.setGeometry(400, 200, 400, 400)

        self.lbl = QtWidgets.QLabel('Картинка', self)
        self.lbl.move(170, 60)
        self.btn = QtWidgets.QPushButton('Жмякнуть', self)
        self.btn.move(150, 90)
        self.btn.clicked.connect(self.pushed)

        self.lbl2 = QtWidgets.QLabel('Картинка(Dead Inside Edition)', self)
        self.lbl2.setGeometry(120, 160, 200, 30)
        self.btn2 = QtWidgets.QPushButton('Жмякнуть', self)
        self.btn2.move(150, 190)
        self.btn2.clicked.connect(self.pushed2)

    def pushed(self):
        image = Image.open(io.BytesIO(self.data))
        image.show()

    def pushed2(self):
        image = Image.open(io.BytesIO(self.data))
        blackAndWhite = image.convert("L")
        blackAndWhite.show()


while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        file = client_sock.recv(1024)
        data = file

        while file:
            file = client_sock.recv(1024)
            data += file

        app = QtWidgets.QApplication(sys.argv)
        mainwindow = MainWindow(data)
        mainwindow.show()
        app.exec()

        break

    client_sock.close()