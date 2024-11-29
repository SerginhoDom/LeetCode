import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        pq = [(0, 0, 0)]
        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            time, x, y = heapq.heappop(pq)

            if (x, y) == (m - 1, n - 1):
                return time

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    wait_time = max(grid[nx][ny] - time, 0)
                    next_time = time + 1 + wait_time
                    heapq.heappush(pq, (next_time, nx, ny))

        return -1