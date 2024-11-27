import math


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u in range(n - 1):
            graph[u].append(u + 1)
        result = []
        distance = list(range(n))
        def min_distance(graph, start):
            for i in range(start, len(graph)):
                for next_node in graph[i]:
                    distance[next_node] = min(distance[next_node], distance[i] + 1)
        for u, v in queries:
            graph[u].append(v)
            if distance[v] > distance[u] + 1:
                distance[v] = distance[u] + 1
                min_distance(graph, v)
            result.append(distance[-1])
        return result