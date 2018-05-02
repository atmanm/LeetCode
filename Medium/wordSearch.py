# Given a 2D board and a word, find if the word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cell, where
#"adjacent" cells are those horizontally or vertically neighboring. The same
#letter cell may not be used more than once.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existHelper(board, word, i, j):
                    return True

        return False

    def existHelper(self, board, word, i, j):
        elem = board[i][j]
        if elem == word[0]:
            if len(word[1:]) == 0:
                return True
            board[i][j] = " "

            if i < len(board) - 1 and self.existHelper(board, word[1:], i+1, j):
                return True
            if i > 0 and self.existHelper(board, word[1:], i-1, j):
                return True
            if j < len(board[0]) - 1 and self.existHelper(board, word[1:], i, j+1):
                return True
            if j > 0 and self.existHelper(board, word[1:], i, j-1):
                return True

            board[i][j] = elem

        return False

if __name__ == "__main__":
    inputBoard = input().strip()
    board = eval(inputBoard)
    word = str(input().strip())

    print(Solution().exist(board, word))
