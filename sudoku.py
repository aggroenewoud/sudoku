import helpers as H

class sudoku:

    def __init__(self, sudoku):

        print(self.check_if_solved(sudoku))

    def cross_hatch(self):

        print()

    def check_if_solved(self, sudoku):

        if sudoku == []:
            return 0

        if H.check_if_empty(sudoku[0]) > 1:
            return 1

        return 0 + self.check_if_solved(sudoku[1:])
