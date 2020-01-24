class SudokuSolver:
    # getSudoku() only for Test use
    def getSudoku(self):
        return [
            [0,4,9,8,0,0,0,3,0],
            [6,8,0,0,0,7,0,0,0],
            [0,2,0,3,9,0,6,0,0],
            [9,0,0,4,0,5,0,8,0],
            [0,0,8,0,0,0,9,0,0],
            [0,1,0,6,0,9,0,0,2],
            [0,0,5,0,6,8,0,7,0],
            [0,0,0,7,0,0,0,6,4],
            [0,7,0,0,0,2,5,9,0]
            ]

    def printSudoku(self, sudoku):
        i = 0
        while i < len(sudoku):
            print(sudoku[i])
            i += 1

    def solve(self, sudoku):
        emptyField = self.findEmpty(sudoku)
        if emptyField:
            y, x = emptyField
        else:
            self.printSudoku(sudoku)
            return True

        i = 1
        while i < 10:
            if self.checkH(sudoku, y, i) and self.checkV(sudoku, x, i):
                sudoku[y][x] = i

                if self.solve(sudoku):
                    return True
            
                sudoku[y][x] = 0
            i += 1
        return False
            

    def findEmpty(self, sudoku):
        y = 0
        while y < 9:
            x = 0
            while x < 9:
                if sudoku[y][x] == 0:
                    return (y, x)
                x += 1
            y += 1

    def checkH(self,sudoku, y, value):
        count = 0
        while count < 9:
            if sudoku[y][count] == value:
                return False
            count += 1
        return True

    def checkV(self,sudoku, x, value):
        count = 0
        while count < 9:
            if sudoku[count][x] == value:
                return False
            count += 1
        return True

