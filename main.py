from PyQt5.QtWidgets import QApplication, qApp
import SudokuSolve
import SudokuWindow
import sys

class Window(SudokuWindow.MainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        print('__init__')
        """
        app = QApplication(sys.argv)
        main_window = SudokuWindow.MainWindow()
        main_window.show()
        sys.exit(app.exec_())
        """


    def ShowCandidate(self):

        print('set style [0][3][0]')
        self.cells[0][0][5].setStyleSheet('border : 2px solid blue')



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