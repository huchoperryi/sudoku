from PyQt5 import QtWidgets
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

        self.cells = []
        cell_width = 27
        for i in range(27*27):
            row = i // cell_width
            col = i % cell_width
            #text = str((i % 3)+ 1 )
            text = str((((i // 27) % 3) * 3) + (i % 3) + 1)
            cell = QtWidgets.QLabel(self)
            cell.setText(text)
            cell.setStyleSheet(style)
            cell.setAlignment(Qt.AlignCenter)
            cell.setFixedSize(15,15)
            self.cells.append(cell)
            self.grid.addWidget(self.cells[i], row, col)
        
        self.setLayout(self.grid)

        #self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle(('ViewSample'))

        #self.cells[0].setStyleSheet("border: 1px solid red;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    time.sleep(3)
    main_window.cells[30].setStyleSheet('border: 1px solid red;')
    sys.exit(app.exec_())
