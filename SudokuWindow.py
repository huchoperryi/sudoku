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
        style = 'background-color : skyblue;'
            #"border: 1px solid black; "

        self.MainFrame = QHBoxLayout()
        self.InputFrame = QVBoxLayout()
        self.TaskFrame = QGridLayout()
        self.WorkFrame = QGridLayout()
        self.grid = QGridLayout()
        self.InputFrame.addLayout(self.TaskFrame)
        self.InputFrame.addLayout(self.WorkFrame)
        self.MainFrame.addLayout(self.InputFrame)
        self.MainFrame.addLayout(self.grid)

        self.work_backs = []


            
        self.SetTaskGrid()
        self.SetWorkGrid()


        self.cell_backs = []

        for i in range(81):
            cell_back = QLabel(self)
            cell_back.move(
                243 + i % 9 * 54 + (i % 9) // 3 * 9,
                9 + i // 9 * 54 + (i // 9) // 3 * 9
                )
            cell_back.setFixedSize(53,53)
            cell_back.setStyleSheet('background-color : #9090c0')
            self.cell_backs.append(cell_back)
            #self.WorkFrame.addWidget(cell_back)

        # create 27 x 27 Labels and add to layout
        self.cells = []
        cell_width = 27
        for row in range(9):
            cols = []
            for col in range(9):
                indexs = []
                for i in range(9):

                    text = str(i + 1)
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


        self.button = QPushButton('Show data', self)
        #self.button.clicked.connect(self.output)
        self.button.clicked.connect(self.ShowCandidate)

        self.grid.addWidget(self.button, 29, 0, 1, 5)

        self.setLayout(self.MainFrame)

        #self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle(('ViewSample'))

        #self.cells[0].setStyleSheet("border: 1px solid red;")

    def SetTaskGrid(self):

        #self.input_grid = QGridLayout(self)
        #self.WorkFrame.addLayout(self.input_grid)
        self.task_backs = []

        for i in range(9):
            task_back = QLabel(self)
            task_back.move(
                9 + i % 3 * 75,
                23 + i // 3 * 72
                )
            task_back.setFixedSize(74,71)
            task_back.setStyleSheet('background-color : #9090c0')
            self.task_backs.append(task_back)
            #self.WorkFrame.addWidget(work_back)

        self.tasks = []
        for row in range(9):
            tmp_tasks = []
            for col in range(9):
                tmp_task = QLineEdit(self)
                tmp_task.setFixedSize(18,18)
                tmp_task.senderSignalIndex = row * 10 + col
                tmp_task.returnPressed.connect(self.TaskReturn)
                tmp_tasks.append(tmp_task)
                self.TaskFrame.addWidget(tmp_task, row, col, 1, 1)
            self.tasks.append(tmp_tasks)
        task_label = QLabel()
        task_label.setText('TaskGrid')
        self.TaskFrame.addWidget(task_label, 9, 0, 1, 3)
        self.solve_button = QPushButton()
        self.solve_button.setText('Solve')
        self.solve_button.clicked.connect(self.SolveTask)
        self.TaskFrame.addWidget(self.solve_button, 9, 3, 1, 3)
        self.reset_button = QPushButton()
        self.reset_button.setText('RESET')
        self.reset_button.clicked.connect(self.ResetTask)
        self.TaskFrame.addWidget(self.reset_button, 9, 6, 1, 3)


    def TaskReturn(self):

        send_obj = self.sender()
        row = send_obj.senderSignalIndex // 10
        col = send_obj.senderSignalIndex % 10

        next_row = (row + (col + 1) // 9) % 9
        next_col = (col + 1) % 9

        value = send_obj.text()
        #print('next_row: {} next_col: {}'.format(next_row, next_col))
        self.tasks[next_row][next_col].setFocus()
        
        self.works[row][col].setText(value)


    def SetWorkGrid(self):
        # self.works : list of QLineEdit

        
        self.work_backs = []

        for i in range(9):
            work_back = QLabel(self)
            work_back.move(
                9 + i % 3 * 75,
                282 + i // 3 * 72
                )
            work_back.setFixedSize(74,71)
            work_back.setStyleSheet('background-color : #9090c0')
            self.work_backs.append(work_back)
            #self.addWidget(work_back)
        

        self.works = []
        for row in range(9):
            tmp_works = []
            for col in range(9):
                tmp_work = QLineEdit(self)
                tmp_work.setFixedSize(18,18)
                tmp_work.senderSignalIndex = row * 10 + col
                tmp_work.returnPressed.connect(self.WorkReturn)
                tmp_works.append(tmp_work)
                self.WorkFrame.addWidget(tmp_work, row, col, 1, 1)
            self.works.append(tmp_works)
        work_label = QLabel()
        work_label.setText('WorkGrid')
        self.WorkFrame.addWidget(work_label, 9, 0, 1, 5)
        self.work_button = QPushButton()
        self.work_button.setText('work_button')
        self.work_button.clicked.connect(self.WorkProcess)
        self.WorkFrame.addWidget(self.work_button, 9, 5, 1, 4)


    def WorkProcess(self):
        
        for row in range(9):
            for col in range(9):
                print(self.works[row][col].text(), end='')
            print('')


    def WorkReturn(self):

        send_obj = self.sender()
        row = send_obj.senderSignalIndex // 10
        col = send_obj.senderSignalIndex % 10
        #print('row: {} col: {}'.format(row, col))

        next_row = (row + (col + 1) // 9) % 9
        next_col = (col + 1) % 9
        #print('next_row: {} next_col: {}'.format(next_row, next_col))
        self.works[next_row][next_col].setFocus()


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
