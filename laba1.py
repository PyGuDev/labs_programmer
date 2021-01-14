from PyQt5 import QtCore, QtWidgets as QW, QtGui, uic
from pyqtgraph import PlotWindow, plot
import numpy as np
import sys
import pyqtgraph as pg


class MainWindow(QW.QMainWindow):
    def __init__(self):
        QW.QMainWindow.__init__(self)
        uic.loadUi('main.ui', self)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        x = np.arange(1)
        self.fives = 0
        self.fours = 0
        self.three = 0
        self.two = 0
        self.bg_fives = pg.BarGraphItem(x=x, height=self.fives, width=0.3, brush='r', name='Fives')
        self.bg_fours = pg.BarGraphItem(x=x + 0.33, height=self.fours, width=0.3, brush='g', name='Четверки')
        self.bg_three = pg.BarGraphItem(x=x + 0.66, height=self.three, width=0.3, brush='b', name='Тройки')
        self.bg_two = pg.BarGraphItem(x=x + 0.99, height=self.two, width=0.3, brush='y', name='Двойки')
        self.graphWidget.addItem(self.bg_fives)
        self.graphWidget.addItem(self.bg_fours)
        self.graphWidget.addItem(self.bg_three)
        self.graphWidget.addItem(self.bg_two)
        self.graphWidget.addLegend()
        self.canvas_layout = QW.QVBoxLayout()
        self.canvas_layout.addWidget(self.graphWidget)
        self.canvasWidget.setLayout(self.canvas_layout)
        self.inp_five.textChanged[str].connect(self.onChangedFive)
        self.inp_four.textChanged[str].connect(self.onChangedFour)
        self.inp_three.textChanged[str].connect(self.onChangedThree)
        self.inp_two.textChanged[str].connect(self.onChangedTwo)

    # Добовление кол-ва пятерок в график
    def onChangedFive(self, text):
        self.fives = int(text)
        self.bg_fives.setOpts(height=self.fives)

    # Добовление кол-ва четверок в график
    def onChangedFour(self, text):
        self.fours = int(text)
        self.bg_fours.setOpts(height=self.fours)

    # Добовление кол-ва трое в график
    def onChangedThree(self, text):
        self.three = int(text)
        self.bg_three.setOpts(height=self.three)

    # Добовление кол-ва двоек в график
    def onChangedTwo(self, text):
        self.two = int(text)
        self.bg_two.setOpts(height=self.two)


if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
