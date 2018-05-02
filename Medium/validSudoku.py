#Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#The Sudoku board could be partially filled, where empty cells are filled with
#the character '.'.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def getListIndices(xIndex, yIndex):
            return xIndex, yIndex, (3*(xIndex//3)+(yIndex//3))

        rowDicts = [{} for i in range(9)]
        colDicts = [{} for i in range(9)]
        boxDicts = [{} for i in range(9)]

        for xIndex, row in enumerate(board):
            for yIndex, entry in enumerate(row):
                if entry is '.':
                    continue
                rowIndex, colIndex, boxIndex = getListIndices(xIndex, yIndex)
                try:
                    xExists = rowDicts[rowIndex][entry]
                except KeyError:
                    rowDicts[rowIndex][entry] = 1
                else:
                    return False
                try:
                    yExists = colDicts[colIndex][entry]
                except KeyError:
                    colDicts[colIndex][entry] = 1
                else:
                    return False
                try:
                    boxExists = boxDicts[boxIndex][entry]
                except KeyError:
                    boxDicts[boxIndex][entry] = 1
                else:
                    return False

        return True

if __name__ == "__main__":
    board = input().strip()
    boardList = eval(board)
    print(Solution().isValidSudoku(boardList))
