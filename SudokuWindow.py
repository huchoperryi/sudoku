from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
import sip
import time

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #self.setStyleSheet('background-color:red;')
        style = "border: 1px solid black; " \
            + "background-color : skyblue;"
        self.MainFrame = QHBoxLayout()
        self.InputFrame = QGridLayout()
        self.grid = QGridLayout()
        self.MainFrame.addLayout(self.InputFrame)
        self.MainFrame.addLayout(self.grid)

        self.SetInputGrid()



        # create 27 x 27 Labels and add to layout
        self.cells = []
        cell_width = 27
        for row in range(9):
            cols = []
            for col in range(9):
                indexs = []
                for i in range(9):

                    text = str(col)
                    index = QtWidgets.QLabel(self)
                    index.setText(text)
                    index.setFont(QtGui.QFont('Ricty Diminished Discord',10))
                    index.setStyleSheet(style)
                    index.setAlignment(Qt.AlignCenter)
                    index.setFixedSize(12,12)
                    indexs.append(index)
                    self.grid.addWidget(index,
                                        row * 3 + i // 3 + row // 3,
                                        col * 3 + i % 3 + col // 3)

                cols.append(indexs)
            self.cells.append(cols)
        
        borders = []
        border_style = "background-color : #4169e1"
        #"border: 1px solid #1e90ff; " \
        #             + "background-color : dadgerblue"
        for i in range(2):
            border = QtWidgets.QLabel(self)
            border.setStyleSheet(border_style)
            border.setFixedWidth(3)
            self.grid.addWidget(border, 0, 9 + 10 * i , 29, 1)
            borders.append(border)

        for i in range(2):
            
            border = QtWidgets.QLabel(self)
            border.setStyleSheet(border_style)
            border.setFixedHeight(3)
            self.grid.addWidget(border, 9 + 10 * i , 0, 1, 29)
            borders.append(border)


        self.button = QPushButton('execute', self)
        #self.button.clicked.connect(self.output)
        self.button.clicked.connect(self.ShowCandidate)

        self.grid.addWidget(self.button, 29, 0, 1, 5)

        self.setLayout(self.MainFrame)

        #self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle(('ViewSample'))

        #self.cells[0].setStyleSheet("border: 1px solid red;")

    def SetInputGrid(self):

        #self.input_grid = QGridLayout(self)
        #self.InputFrame.addLayout(self.input_grid)
        self.inputs = []
        self.input = QLineEdit(self)
        self.InputFrame.addWidget(self.input, 0, 0)


    def output(self):
        print('clicked')
        self.cells[1][1][0].setStyleSheet('border: 1px solid red;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    #time.sleep(3)
    main_window.cells[0][0][0].setStyleSheet('border: 1px solid red;')
    main_window.cells[0][0][1].hide()
    sys.exit(app.exec_())
