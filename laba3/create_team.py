import sys
from PyQt5 import QtCore, QtWidgets as QW, uic
import random


class CreateTeamWidget(QW.QWidget):
    def __init__(self):
        QW.QWidget.__init__(self)
        uic.loadUi('create_teams.ui', self)
        self.pushButton.clicked.connect(self.creaet_players)

    def creaet_players(self):
        self.count_player = int(self.lineEdit.text())
        save_player_widget = SavePlayerWidget(self.count_player)
        save_player_widget.show()
        self.close()


class SavePlayerWidget(QW.QWidget):
    def __init__(self, count_player):
        QW.QWidget.__init__(self)
        uic.loadUi('players.ui', self)
        self.count_player = count_player
        self.players_layout = QW.QVBoxLayout()
        for i in range(self.count_player):
            self.players_layout.addLayout(PlayerWidget())
        self.setLayout(self.players_layout)
        self.btn_search_shoe_in_shop = QW.QPushButton('Искать обувь в мазине')
        self.btn_search_shoe_in_shop.clicked.connect(self.search_shoe_in_shop)
        self.players_layout.addWidget(self.btn_search_shoe_in_shop)

    def search_shoe_in_shop(self):
        self.shop = CreateShoeShop()
        self.shop.show()
        self.close()


class PlayerWidget(QW.QHBoxLayout):
    def __init__(self):
        QW.QHBoxLayout.__init__(self)
        self.input_name = QW.QLineEdit()
        self.input_name.setPlaceholderText('Имя игрока')
        self.input_shoe_size = QW.QLineEdit()
        self.input_shoe_size.setPlaceholderText('Размер обуви')
        self.addWidget(self.input_name)
        self.addWidget(self.input_shoe_size)

    def get_shoe_size(self):
        return self.input_shoe_size.text()


class CreateShoeShop(QW.QWidget):
    def __init__(self):
        QW.QWidget.__init__(self)
        uic.loadUi('create_shop.ui', self)
        self.add_shoe.clicked.connect(self.generate_shoe)
        self.shoes = []

    def generate_shoe(self):
        self.count_shoe = int(self.input_count_shoe.text())
        self.shoes = [random.randint(39, 45) for i in range(self.count_shoe)]

    def get_shoes(self):
        return self.count_shoe



if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    create_widget = CreateTeamWidget()
    create_widget.show()
    app.exec_()