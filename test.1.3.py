import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QRect


class DrawingAPattern(QWidget):
    """Класс рисования узоров"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Лаба1 задание 3')
        self.show()
        self.resize(640, 480)

    # Переопределение события рисования
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    # Метод ресования
    def drawBrushes(self, qp):
        for i in range(100):
            # Определяем объект кисти с с рандомным цветом
            brush = QBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0,255)), Qt.SolidPattern)
            qp.setBrush(brush)
            # Берем рандомные значения радиуса и положения x, y
            r = random.randint(40, 100)
            x = random.randint(40, 600)
            y = random.randint(40, 440)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawingAPattern()
    sys.exit(app.exec_())
