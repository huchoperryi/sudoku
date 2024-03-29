from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
import sip
import time

class ClickableLabel(QLabel):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(ClickableLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        return QLabel.mousePressEvent(self, event)


class MainWindow(QWidget):
    # self.tasks[9][9] task set Qlineedit
    # self.works[9][9] work set Qlineedit
    # self.cells[9][9] display candidates

    def __init__(self, parent=None): # windowの初期生成
        super(MainWindow, self).__init__(parent)


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

        self.SetCellGrid()
        self.SetTaskGrid()
        self.SetWorkGrid()



        self.button = QPushButton('Show data', self)
        #self.button.clicked.connect(self.output)
        self.button.clicked.connect(self.ShowCandidate)

        self.grid.addWidget(self.button, 29, 0, 1, 5)

        self.setLayout(self.MainFrame)

        #self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle(('Sudoku Solve'))

        #self.cells[0].setStyleSheet("border: 1px solid red;")

        self.message_box = QtWidgets.QTextEdit(self)
        self.MainFrame.addWidget(self.message_box)

    def SetCellGrid(self):
    
        #self.setStyleSheet('background-color:red;')
        style = 'background-color : skyblue;'
            #"border: 1px solid black; "
    
        self.cell_backs = []
    
        for i in range(81):
            cell_back = QLabel(self)
            cell_back.move(
                225 + i % 9 * 54 + (i % 9) // 3 * 9,
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
                    index = ClickableLabel(self)
                    index.setText(text)
                    index.setFont(QtGui.QFont('Ricty Diminished Discord',10))
                    index.setStyleSheet(style)
                    index.setAlignment(Qt.AlignCenter)
                    index.setFixedSize(12,12)
                    index.senderSignalIndex = 1000 + row * 100 + col * 10 + i
                    index.clicked.connect(self.CellClicked)
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
    

    def CellClicked(self):
        send_obj = self.sender()
        id = send_obj.senderSignalIndex
        row = (id - 1000) // 100
        col = (id % 100) // 10
        index = id % 10
        grey = 'background-color : grey'

        self.message_box.append('Cell clicked row:{} col:{} index:{}'.format(row, col, index))
        self.cells[row][col][index].setStyleSheet(grey)


    def SetTaskGrid(self): # task入力欄の生成

        #self.input_grid = QGridLayout(self)
        #self.WorkFrame.addLayout(self.input_grid)
        self.task_backs = []

        for i in range(9):
            task_back = QLabel(self)
            task_back.move(
                9 + i % 3 * 72,
                23 + i // 3 * 72
                )
            task_back.setFixedSize(71,71)
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
        task_label.setFixedWidth(65)
        task_label.setText('TaskGrid')
        self.TaskFrame.addWidget(task_label, 9, 0, 1, 3)
        self.solve_button = QPushButton()
        self.solve_button.setFixedWidth(65)
        self.solve_button.setText('Solve')
        self.solve_button.clicked.connect(self.SolveTask)
        self.TaskFrame.addWidget(self.solve_button, 9, 3, 1, 3)
        self.reset_button = QPushButton()
        self.reset_button.setText('RESET')
        self.reset_button.setFixedWidth(65)
        self.reset_button.clicked.connect(self.ResetTask)
        self.TaskFrame.addWidget(self.reset_button, 9, 6, 1, 3)


    def TaskReturn(self): # task 入力欄でreturn入力時に実行

        # sender().senderSignalIndexから入力欄の位置を判定
        send_obj = self.sender()
        row = send_obj.senderSignalIndex // 10
        col = send_obj.senderSignalIndex % 10

        # 一つ右 右端なら1行下の左端へ移動
        next_row = (row + (col + 1) // 9) % 9
        next_col = (col + 1) % 9

        value = send_obj.text()
        #print('next_row: {} next_col: {}'.format(next_row, next_col))
        self.tasks[next_row][next_col].setFocus()
        
        self.works[row][col].setText(value)

        if (value != '' and value != ' '):
            self.message_box.append('set task')

        self.SolveTask()


    def GetList(self, cells): # task,workの値リストを返す

        cell_values = []
        for row in range(9):
            cell_value = []
            for col in range(9):
                value = cells[row][col].text()
                if (value == '' or value == ' '):
                    value = 0
                else:
                    value = int(value)
                cell_value.append(value)
            cell_values.append(cell_value)
        return cell_values


    def SetWorkGrid(self): # work入力欄の生成
        # self.works : list of QLineEdit

        
        self.work_backs = []

        for i in range(9):
            work_back = QLabel(self)
            work_back.move(
                9 + i % 3 * 72,
                282 + i // 3 * 72
                )
            work_back.setFixedSize(71,71)
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
        work_label.setFixedWidth(65)
        work_label.setText('WorkGrid')
        self.WorkFrame.addWidget(work_label, 9, 0, 1, 3)
        self.work_button = QPushButton()
        self.work_button.setFixedWidth(65)
        self.work_button.setText('work_button')
        self.work_button.clicked.connect(self.WorkProcess)
        self.WorkFrame.addWidget(self.work_button, 9, 3, 1, 3)


    def WorkProcess(self): # 
        
        for row in range(9):
            for col in range(9):
                print(self.works[row][col].text(), end='')
            print('')


    def WorkReturn(self): # work入力欄でreturn入力時に実行

        # sender().senderSignalIndexから入力欄の位置を判定
        send_obj = self.sender()
        row = send_obj.senderSignalIndex // 10
        col = send_obj.senderSignalIndex % 10
        #print('row: {} col: {}'.format(row, col))

        # 一つ右 右端なら1行下の左端へ移動
        next_row = (row + (col + 1) // 9) % 9
        next_col = (col + 1) % 9
        #print('next_row: {} next_col: {}'.format(next_row, next_col))
        self.works[next_row][next_col].setFocus()


    def output(self): # テスト用に作ってたやつ
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
