class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        rows, cols = len(grid), len(grid[0])

        def isOutside(x, y):
            return x < 0 or x >= rows or y < 0 or y >= cols

        def idx(x, y):
            return x * cols + y

        total_cells = rows * cols
        time = [2**31] * total_cells
        pq = [0]

        time[0] = 0
        while len(pq):
            current = heappop(pq)
            t, cell_idx = current >> 32, current & ((1 << 30) - 1)
            x, y = divmod(cell_idx, cols)
            if x == rows - 1 and y == cols - 1:
                return t

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if isOutside(nx, ny):
                    continue

                wait_time = 0 if (grid[nx][ny] - t) & 1 else 1
                nextTime = max(t + 1, grid[nx][ny] + wait_time)

                next_cell = idx(nx, ny)
                if nextTime < time[next_cell]:
                    time[next_cell] = nextTime
                    heappush(pq, (nextTime << 32) + next_cell)
        return -1