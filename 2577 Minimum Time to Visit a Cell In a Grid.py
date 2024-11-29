class Solution:
    def traverse_table(self, matrix, x, y, time):
        rows, cols = len(matrix), len(matrix[0])

        if x == rows - 1 and y == cols - 1:
            return time

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if matrix[nx][ny] <= time:
                    self.traverse_table(matrix, nx, ny, time + 1)


    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return - 1
        traverse_table(grid, 0, 0, 1)