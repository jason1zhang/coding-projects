from typing import List


class LCMatrix:

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
