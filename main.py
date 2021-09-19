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



        self.SetTaskWorkGUI(self.works)


    def SetTaskWorkGUI(self, input_grid):
        
        for row in range(9):
            for col in range(9):
                value = self.field.rows[row][col].value
                input_grid[row][col].setText(str(value))
                #self.tasks[row][col].setText(str(value))
                #self.works[row][col].setText(str(value))



    def ShowCandidate(self):

        for row in range(9):
            for col in range(9):
                for index in range(9):
                    if self.field.rows[row][col].judge[index]:
                        self.cells[row][col][index].setStyleSheet("background-color : skyblue")
                    else:
                        self.cells[row][col][index].setStyleSheet("background-color : grey")

    def SolveTask(self):
        self.field.Solve()
        self.SetTaskWorkGUI(self.works)

    def ResetTask(self):

        print('ResetTask')


    def TaskSet(self):
        task = [[0,0,0, 0,0,0, 9,0,0],
                [0,0,0, 4,9,0, 0,0,6],
                [0,9,6, 0,0,0, 0,4,0],
                [0,0,0, 0,8,0, 7,0,0],
                [0,2,0, 0,3,7, 5,1,0],
                [5,0,0, 0,2,0, 3,8,0],
                [9,6,0, 1,0,0, 4,0,0],
                [8,5,4, 0,7,0, 0,2,1],
                [0,3,0, 0,0,0, 0,0,0]]
        return task




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