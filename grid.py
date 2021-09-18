from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip
import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.cell1 = QtWidgets.QLabel(self)
        self.cell1.setText('1')
        self.cell1.setFixedSize(15, 15)
        self.cell2 = QtWidgets.QLabel(self)
        self.cell2.setText('1')
        self.cell2.setFixedSize(15, 15)

        self.grid = QGridLayout()

        self.grid.addWidget(self.cell1, 0, 0)
        self.grid.addWidget(self.cell2, 1, 3)

        self.setLayout(self.grid)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())