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
        style = "border: 1px solid black;"
        
        self.grid = QGridLayout()

        # create 27 x 27 Labels and add to layout
        self.cells = []
        cell_width = 27
        for i in range(27*27):
            row = i // cell_width
            col = i % cell_width
            #text = str((i % 3)+ 1 )
            text = str((((i // 27) % 3) * 3) + (i % 3) + 1)
            cell = QtWidgets.QLabel(self)
            cell.setText(text)
            cell.setFont(QtGui.QFont('Ricty Diminished Discord',10))
            #cell.setStyleSheet(style)
            cell.setAlignment(Qt.AlignCenter)
            cell.setFixedSize(12,12)
            self.cells.append(cell)
            self.grid.addWidget(self.cells[i], row, col)
        
        self.button = QPushButton('execute', self)
        self.button.clicked.connect(self.output)

        self.grid.addWidget(self.button, 27, 0, 1, 5)

        self.setLayout(self.grid)

        #self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle(('ViewSample'))

        #self.cells[0].setStyleSheet("border: 1px solid red;")

    def output(self):
        print('clicked')
        self.cells[4].setStyleSheet('border: 1px solid red;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    #time.sleep(3)
    main_window.cells[30].setStyleSheet('border: 1px solid red;')
    main_window.cells[31].hide()
    sys.exit(app.exec_())
