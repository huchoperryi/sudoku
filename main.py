from PyQt5.QtWidgets import QApplication, qApp
import SudokuSolve
import SudokuWindow
import sys

class Window(SudokuWindow.MainWindow):

    style_bg_grey = "background-color : grey"
    style_bg_skyblue = "background-color : skyblue"

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        print('__init__')
        """
        app = QApplication(sys.argv)
        main_window = SudokuWindow.MainWindow()
        main_window.show()
        sys.exit(app.exec_())
        """

        self.field = SudokuSolve.SudokuField()
        self.field.SetTask(self.TaskSet())
        self.field.show()

        self.SetTaskWorkGUI(self.tasks)
        self.SetTaskWorkGUI(self.works)


    def SetTaskWorkGUI(self, input_grid): # task/workにfield値を入れる
        
        for row in range(9):
            for col in range(9):
                value = self.field.rows[row][col].value
                if value == ' ':
                    value = ''
                input_grid[row][col].setText(str(value))
                #self.tasks[row][col].setText(str(value))
                #self.works[row][col].setText(str(value))


    def ResetTask(self):
        self.field.Reset()
        self.SetTaskWorkGUI(self.tasks)
        self.SetTaskWorkGUI(self.works)
        print('ResetTask')
        self.field.ShowWithCandidate()


    def ShowCandidate(self):

        skyblue = 'background-color : skyblue'
        grey = 'background-color : grey'
        redborder = 'border: 1px solid red ; background-color : skyblue'
        for row in range(9):
            for col in range(9):
                for index in range(9):
                    field_cell = self.field.rows[row][col]
                    grid_cell = self.cells[row][col]

                    if (field_cell.value == index + 1 and
                        field_cell.is_fixed == True):
                        grid_cell[index].setStyleSheet(redborder)
                    elif field_cell.judge[index]:
                        grid_cell[index].setStyleSheet(skyblue)
                    else:
                        grid_cell[index].setStyleSheet(grey)

    def SolveTask(self):

        # 一度初期化する
        self.field.Reset()

        # tasksの数値をworksにコピー
        for row in range(9):
            for col in range(9):
                value = self.tasks[row][col].text()
                self.works[row][col].setText(value)

        # worksの数値をsolverにセット
        for row in range(9):
            for col in range(9):

                value = self.works[row][col].text()
                if value == '':
                    value = ' '

                if (49 <= ord(value) and ord(value) <= 57):
                    value = int(value)
                    self.field.rows[row][col].SetValue(value)
                    msg = 'set value row:{} col:{} value:{}'
                    print(msg.format(row, col, value))
        count = self.field.Solve()
        if count != 0:
            self.message_box.append('{} cells fixed!'.format(count))
        self.SetTaskWorkGUI(self.works)
        self.ShowCandidate()


    def TaskSet(self):
        task = [[0,0,0, 0,0,0, 6,0,0],
                [0,0,6, 0,1,0, 9,0,0],
                [7,0,0, 8,2,0, 0,5,0],
                [0,5,0, 0,4,0, 0,0,3],
                [6,2,3, 1,0,7, 0,0,0],
                [0,4,0, 0,5,0, 0,0,9],
                [4,0,0, 5,3,0, 0,2,0],
                [0,0,1, 0,6,0, 8,0,0],
                [0,0,0, 0,0,0, 5,0,0]]
        return task
        """
               [[0,0,0, 0,0,0, 6,0,0],
                [0,0,6, 0,1,0, 9,0,0],
                [7,0,0, 8,2,0, 0,5,0],
                [0,5,0, 0,4,0, 0,0,3],
                [6,2,3, 1,0,7, 0,0,0],
                [0,4,0, 0,5,0, 0,0,9],
                [4,0,0, 5,3,0, 1,2,0], 6番目:1
                [0,0,1, 0,6,0, 8,0,0],
                [0,0,0, 0,0,0, 5,0,0]] 6番目:5 2か所入ると解ける
        """




if __name__ == '__main__':

    app = QApplication(sys.argv)
    sudoku_window = Window()
    sudoku_window.show()
    #sudoku_window.ShowCandidate()
    sys.exit(app.exec_())

    field = SudokuSolve.SudokuField()
    print('set task')
    field.SetTask()
    field.show()
    #field.ShowWithCandidate()
    print('solve')
    field.Solve()
    field.show()
    #field.ShowWithCandidate()