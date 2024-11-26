class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        in_degree = [0] * n

        for u, v in edges:
            in_degree[v] += 1

        champion = -1

        for i in range(n):
            if in_degree[i] == 0:
                if champion != -1:
                    return -1
                champion = i

        return champion