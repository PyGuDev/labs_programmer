from PyQt5 import QtCore, QtWidgets as QW, QtGui, uic
import sys


class TeamsWidget(QW.QWidget):
    def __init__(self):
        QW.QWidget.__init__(self)
        self.__main_label = QW.QLabel('Батскетбольная команда')
        self.__main_layout = QW.QGridLayout()
        self.__main_layout.addWidget(self.__main_label)
        self.__input_count_players = QW.QLineEdit()
        self.__input_count_players.setPlaceholderText('Кол-во игроков')
        self.__btn_add_player = QW.QPushButton(text='Добавить')
        self.__btn_add_player.clicked.connect(self.create_teams)
        self.__main_layout.addWidget(self.__input_count_players)
        self.__main_layout.addWidget(self.__btn_add_player)
        self.setLayout(self.__main_layout)
        self.btn_go_to_shop = QW.QPushButton('Перейти в магазин')

    def create_teams(self):
        count_player = self.__input_count_players.text()
        positions = [(x, 0) for x in range(3, int(count_player) + 3,)]
        players = [TeamPlayersWidget() for x in range(int(count_player))]
        for position, player in zip(positions, players):
            self.__main_layout.addLayout(player, *position)
        self.__main_layout.addWidget(self.__btn_go_to_shop)


class TeamPlayersWidget(QW.QHBoxLayout):
    def __init__(self, parent=None):
        super(TeamPlayersWidget, self).__init__(parent)
        self.__shoe_size = QW.QLineEdit()
        self.__shoe_size.setPlaceholderText('Размер обуви')
        self.__name = QW.QLineEdit()
        self.__name.setPlaceholderText('Имя')
        self.addWidget(self.__name)
        self.addWidget(self.__shoe_size)

    def get_shoe_size(self):
        return self.__shoe_size


class ShoeStoreWidget(QW.QWidget):
    def __init__(self, parent=None):
        super(ShoeStoreWidget, self).__init__(parent)
        self.__main_label = QW.QLabel('Обувной магазин')
        self.__main_layout = QW.QGridLayout()
        self.__count_sport_shoes = QW.QLineEdit()
        self.__count_sport_shoes.setPlaceholderText('Кол-во спортивной обуви')
        self.btn_add_shoes = QW.QPushButton('Добавить')
        self.btn_add_shoes.clicked.connect(self.create_teams)
        self.__main_layout.addWidget(self.__main_label)
        self.__main_layout.addWidget(self.__count_sport_shoes)
        self.__main_layout.addWidget(self.btn_add_shoes)
        self.setLayout(self.__main_layout)

    def create_teams(self):
        count_sport_shoe = self.__count_sport_shoes.text()
        print(count_sport_shoe)
        positions = [(x, 0) for x in range(3, int(count_sport_shoe) + 3,)]
        shoes = [ShoeWidget() for x in range(int(count_sport_shoe))]
        for position, shoe in zip(positions, shoes):
            self.__main_layout.addLayout(shoe, *position)


class ShoeWidget(QW.QHBoxLayout):
    def __init__(self, parent=None):
        super(ShoeWidget, self).__init__(parent)
        self.__shoe_size = QW.QLineEdit()
        self.__shoe_size.setPlaceholderText('Размер обуви')
        self.addWidget(self.__shoe_size)

    def get_shoe_size(self):
        return self.__shoe_size


class MainWindow(QW.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.teams_widget = TeamsWidget()
        self.shop_widget = ShoeStoreWidget()
        self.main_midget = QW.QStackedWidget(self.teams_widget)
        self.setCentralWidget(self.teams_widget)


if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()