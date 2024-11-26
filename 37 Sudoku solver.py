class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(index=0):
            if index == len(empty_cells):
                return True

            row, col = empty_cells[index]
            box_index = (row // 3) * 3 + col // 3

            for num in map(str, range(1, 10)):
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_index]:
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_index].add(num)

                    if backtrack(index + 1):
                        return True

                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack()
