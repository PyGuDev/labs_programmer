import sys
from PyQt5 import QtCore, QtWidgets as QW, uic
import random


class CreateTeamWidget(QW.QWidget):
    """
    Окно созданием команды
    Задается кол-во игроков
    """
    def __init__(self):
        QW.QWidget.__init__(self)
        uic.loadUi('create_teams.ui', self)
        self.pushButton.clicked.connect(self.next_widget)

    def next_widget(self):
        # Переход на другое окно
        self.count_player = int(self.lineEdit.text())
        save_player_widget = SavePlayerWidget(self.count_player)
        save_player_widget.show()
        self.close()


class SavePlayerWidget(QW.QWidget):
    """
    Окно генерация игроков
    """
    def __init__(self, count_player):
        QW.QWidget.__init__(self)
        uic.loadUi('players.ui', self)
        self.count_player = count_player
        self.players_layout = QW.QVBoxLayout()
        self.size_shoe_players = []
        for i in range(self.count_player):
            self.players_layout.addLayout(PlayerWidget())
        self.setLayout(self.players_layout)
        self.btn_search_shoe_in_shop = QW.QPushButton('Искать обувь в мазине')
        self.btn_search_shoe_in_shop.clicked.connect(self.next_widget)
        self.players_layout.addWidget(self.btn_search_shoe_in_shop)

    def get_shoes_all_player(self):
        # Получение размера всех игрково
        widgets = self.players_layout.findChildren(PlayerWidget)
        self.size_shoe_players = [widget.get_shoe_size() for widget in widgets]
        return self.size_shoe_players

    def next_widget(self):
        # Переход на другое окно
        self.shop = CreateShoeShop(self.get_shoes_all_player())
        self.shop.show()
        self.close()


class PlayerWidget(QW.QHBoxLayout):
    """
    Виджет игрока
    """
    def __init__(self):
        QW.QHBoxLayout.__init__(self)
        self.input_name = QW.QLineEdit()
        self.input_name.setPlaceholderText('Имя игрока')
        self.input_shoe_size = QW.QLineEdit()
        self.input_shoe_size.setPlaceholderText('Размер обуви')
        self.addWidget(self.input_name)
        self.addWidget(self.input_shoe_size)

    def get_shoe_size(self):
        return int(self.input_shoe_size.text())


class CreateShoeShop(QW.QWidget):
    """
    Окно создания магазина
    """
    def __init__(self, shoe_size_all_players):
        QW.QWidget.__init__(self)
        uic.loadUi('create_shop.ui', self)
        self.add_shoe.clicked.connect(self.generate_shoe)
        self.shoe_size_all_players = shoe_size_all_players
        self.shoes_size = []

    def generate_shoe(self):
        # Рандомная генерация игрока
        self.count_shoe = int(self.input_count_shoe.text())
        self.shoes_size = [random.randint(39, 45) for i in range(self.count_shoe)]
        count_curent_shoe = 0
        for shoe_size in self.shoes_size:
            if shoe_size in self.shoe_size_all_players:
                count_curent_shoe += 1
        self.result_widget = ResultWidget(self.shoes_size.__len__(), count_curent_shoe)
        self.result_widget.show()
        self.close()


class ResultWidget(QW.QWidget):
    """
    Окно вывода резултата
    """
    def __init__(self, count_shoe, count_curent_shoe):
        QW.QWidget.__init__(self)
        uic.loadUi('result.ui', self)
        self.count_shoe.setText(str(count_shoe))
        self.count_curent_shoe.setText(str(count_curent_shoe))


if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    create_widget = CreateTeamWidget()
    create_widget.show()
    app.exec_()