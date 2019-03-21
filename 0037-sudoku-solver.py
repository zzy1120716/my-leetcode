"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:
The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 记录每个行、列、方框中已使用的数字，
        # 1代表已使用，0代表未使用
        rows = [[0] * 10 for _ in range(9)]
        cols = [[0] * 10 for _ in range(9)]
        boxes = [[0] * 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]

                if c != '.':
                    num = ord(c) - ord('0')
                    bx = j // 3
                    by = i // 3
                    rows[i][num] = 1
                    cols[j][num] = 1
                    boxes[by * 3 + bx][num] = 1

        self.fill(board, 0, 0, rows, cols, boxes)

    def fill(self, board, x, y, rows, cols, boxes):
        if y == 9:
            return True

        nx = (x + 1) % 9
        ny = y + 1 if nx == 0 else y

        if board[y][x] != '.':
            return self.fill(board, nx, ny, rows, cols, boxes)

        for i in range(1, 10):
            bx = x // 3
            by = y // 3
            box_key = by * 3 + bx
            if not rows[y][i] and not cols[x][i] and not boxes[box_key][i]:
                rows[y][i] = 1
                cols[x][i] = 1
                boxes[box_key][i] = 1
                board[y][x] = chr(i + ord('0'))
                if self.fill(board, nx, ny, rows, cols, boxes):
                    return True
                # backtracking
                board[y][x] = '.'
                boxes[box_key][i] = 0
                cols[x][i] = 0
                rows[y][i] = 0

        return False


# TODO 自己的方法不通过
class Solution1:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = col = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    row = i
                    col = j
        self.dfs(board, [(row, col)], row, col)

    def dfs(self, board, steps, row, col):
        if self.isFinished(board):
            return
        choices = self.findChoices(board, row, col)
        if not choices:
            if not steps:
                return
            else:
                # backtracking
                r, c = steps.pop()
                board[r][c] = '.'
        for c in choices:
            board[row][col] = c
            for i in range(row + 1, 9):
                for j in range(col + 1, 9):
                    if board[i][j] != '.':
                        steps.append((i, j))
                        self.dfs(board, steps, i, j)

    def isFinished(self, board):
        for i in range(9):
            if '.' in board[i]:
                return False
        return True

    def findChoices(self, board, row, col):
        """
        @return: A list of possible choices for one cell.
        """
        choices = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for num in board[row]:
            choices.discard(num)
        for i in range(9):
            choices.discard(board[row][i])
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                choices.discard(board[row // 3 * 3 + i][col // 3 * 3 + j])
        return list(choices)

    def isValidSudoku(self, board):
        for i in range(len(board)):
            if not self.isUnique(board[i]):
                return False
        for i in range(len(board[0])):
            digits = []
            for j in range(len(board)):
                digits.append(board[j][i])
            if not self.isUnique(digits):
                return False
        new_board = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                new_board[i // 3 * 3 + j // 3].append(board[i][j])
        for line in new_board:
            if not self.isUnique(line):
                return False
        return True

    def isUnique(self, digits):
        s = set()
        cnt = 0
        for ch in digits:
            if ord('1') <= ord(ch) <= ord('9'):
                cnt += 1
                s.add(ch)
            elif ch != '.':
                return False
        return len(s) == cnt


if __name__ == '__main__':
    matrix = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(matrix)
    print(matrix)
