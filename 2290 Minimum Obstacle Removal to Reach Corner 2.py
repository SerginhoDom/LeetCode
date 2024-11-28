from collections import deque


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))

        while queue:
            current_cost, current_row, current_col = queue.popleft()

            if current_row == rows - 1 and current_col == cols - 1:
                return current_cost

            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc

                if not (0 <= new_row < rows and 0 <= new_col < cols) or (new_row, new_col) in visited:
                    continue

                visited.add((new_row, new_col))

                if grid[new_row][new_col] == 1:
                    queue.append((current_cost + 1, new_row, new_col))
                else:
                    queue.appendleft((current_cost, new_row, new_col))

        return -1