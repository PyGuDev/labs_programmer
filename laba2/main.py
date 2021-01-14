from PyQt5 import QtCore, QtWidgets as QW, QtGui, uic
import sys
import random


class MainWindow(QW.QMainWindow):
    def __init__(self):
        QW.QMainWindow.__init__(self)
        uic.loadUi('main.ui', self)
        # Количество примеров
        self.number_example = 20
        self.generate_example()
        self.resultLayout = QW.QHBoxLayout()
        self.btn_result = QW.QPushButton('Результат')
        self.btn_result.clicked.connect(self.result)
        self.resultLabel = QW.QLabel('Ответ')
        self.resultLabel.setFont(QtGui.QFont('Arial', 12))
        self.resultLayout.addWidget(self.resultLabel)
        self.resultLayout.addWidget(self.btn_result)
        self.gridLayout.addLayout(QW.QHBoxLayout(), 11, 2)
        self.gridLayout.addLayout(self.resultLayout, 12, 2)

    # Генерация примеров
    def generate_example(self):
        names = ['{} * {} = '.format(random.randint(0, 10), random.randint(0, 10)) for i in range(self.number_example)]
        positions = [(x, y) for x in range(self.number_example // 2) for y in range(self.number_example // 10)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            self.gridLayout.addLayout(Example_task(name), *position)


    # Обработка результатов
    def result(self):
        children = self.gridLayout.findChildren(Example_task)
        curent_answer_count = 0

        for widget in children:
            widget.check_answer()
            if widget.correct_answer:
                curent_answer_count += 1
        if curent_answer_count >= 10:
            self.resultLabel.setText('Отлично')
            self.resultLabel.setStyleSheet('color: green')
        elif 9 >= curent_answer_count >= 8:
            self.resultLabel.setText('Хорошо')
            self.resultLabel.setStyleSheet('color: green')
        elif 7 >= curent_answer_count >= 6:
            self.resultLabel.setText('Удовлетворительно')
            self.resultLabel.setStyleSheet('color: orange')
        elif curent_answer_count < 6:
            self.resultLabel.setText('Плохо')
            self.resultLabel.setStyleSheet('color: red')


# Класс примера лайбел с заданием и поле ввода
class Example_task(QW.QHBoxLayout):
    def __init__(self, name, parent=None):
        super(Example_task, self).__init__(parent)
        self.label = QW.QLabel(name)
        self.label.setFont(QtGui.QFont('Arial', 10))
        self.label.setMinimumWidth(80)
        self.input = QW.QLineEdit()
        self.input.setStyleSheet('background: none; width: 5px')
        self.label_block = QW.QLabel()
        self.label_block.setMinimumWidth(100)
        self.addWidget(self.label)
        self.addWidget(self.input)
        self.addWidget(self.label_block)
        self.correct_answer = False

    # Проверка на правильный ответ
    def check_answer(self):
        x, y = self.label.text().split(' =')[0].split(' * ')
        answer = int(x) * int(y)
        if self.input.text() != '':
            if int(self.input.text()) == answer:
                self.correct_answer = True
            else:
                self.correct_answer = False


if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()