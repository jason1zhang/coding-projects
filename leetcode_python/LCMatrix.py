from typing import List


class LCMatrix:
    @staticmethod
    def game_of_life(board: List[List[int]]) -> None:
        """
        Leet code # 289

        According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
        devised by the British mathematician John Horton Conway in 1970."

        The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1)
        or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
        using the following four rules (taken from the above Wikipedia article):

           - Any live cell with fewer than two live neighbors dies as if caused by under-population.
           - Any live cell with two or three live neighbors lives on to the next generation.
           - Any live cell with more than three live neighbors dies, as if by over-population.
           - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        The next state is created by applying the above rules simultaneously to every cell in the current state,
        where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0

                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]

                    if (rows > r >= 0) and (cols > c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1

                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


    @staticmethod
    def set_zeroes(matrix: List[List[int]]) -> None:
        """
        Leet Code # 73
        Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

        You must do it in place.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Leet Code # 48

        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


    @staticmethod
    def spiral_order(matrix: List[List[int]]) -> List[int]:
        """
        Leet code # 54

        Given an m x n matrix, return all elements of the matrix in spiral order.
        """
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0

        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]

            if not(0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4

            row += directions[directionIndex][0]
            column += directions[directionIndex][1]

        return order

    @staticmethod
    def is_valid_sudoku(board: List[List[str]]) -> bool:
        """
        Leet code # 36

        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
            - Each row must contain the digits 1-9 without repetition.
            - Each column must contain the digits 1-9 without repetition.
            - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:
            A Sudoku board (partially filled) could be valid but is not necessarily solvable.
            Only the filled cells need to be validated according to the mentioned rules.
        """
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    b = (i // 3) * 3 + j // 3

                    if row[i][num] or col[j][num] or block[b][num]:
                        return False

                    row[i][num] = col[j][num] = block[b][num] = 1

        return True
