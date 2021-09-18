from PyQt5 import QtWidgets
#from main import MainWindow
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
import sip

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        style = "border: 1px solid black;"
        self.cell1 = QtWidgets.QLabel(self)
        self.cell1.setText('1')
        self.cell1.setStyleSheet(style)
        self.cell2 = QtWidgets.QLabel(self)
        self.cell2.setText('2')
        self.cell2.setStyleSheet(style)
        self.cell3 = QtWidgets.QLabel(self)
        self.cell3.setText('3')
        self.cell3.setStyleSheet(style)
        self.cell4 = QtWidgets.QLabel(self)
        self.cell4.setText('4')
        self.cell4.setStyleSheet(style)
        self.cell5 = QtWidgets.QLabel(self)
        self.cell5.setText('5')
        self.cell5.setStyleSheet(style)
        self.cell6 = QtWidgets.QLabel(self)
        self.cell6.setText('6')
        self.cell6.setStyleSheet(style)
        self.cell7 = QtWidgets.QLabel(self)
        self.cell7.setText('7')
        self.cell7.setStyleSheet(style)
        self.cell8 = QtWidgets.QLabel(self)
        self.cell8.setText('8')
        self.cell8.setStyleSheet(style)
        self.cell9 = QtWidgets.QLabel(self)
        self.cell9.setText('9')
        self.cell9.setStyleSheet(style)
        
        self.cell1.setFixedSize(15,15)
        self.cell2.setFixedSize(15,15)
        self.cell3.setFixedSize(15,15)
        self.cell4.setFixedSize(15,15)
        self.cell5.setFixedSize(15,15)
        self.cell6.setFixedSize(15,15)
        self.cell7.setFixedSize(15,15)
        self.cell8.setFixedSize(15,15)
        self.cell9.setFixedSize(15,15)
        

        self.horizon1 = QHBoxLayout()
        self.horizon1.addWidget(self.cell1)
        self.horizon1.addWidget(self.cell2)
        self.horizon1.addWidget(self.cell3)
        self.horizon2 = QHBoxLayout()
        self.horizon2.addWidget(self.cell4)
        self.horizon2.addWidget(self.cell5)
        self.horizon2.addWidget(self.cell6)
        self.horizon3 = QHBoxLayout()
        self.horizon3.addWidget(self.cell7)
        self.horizon3.addWidget(self.cell8)
        self.horizon3.addWidget(self.cell9)
        self.vertical = QVBoxLayout()
        
        #self.vertical.SetFixedSize(200, 500)

        self.vertical.addLayout(self.horizon1)
        self.vertical.addLayout(self.horizon2)
        self.vertical.addLayout(self.horizon3)
        
        self.setLayout(self.vertical)

        #self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle(('ViewSample'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
