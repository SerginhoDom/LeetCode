from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        TARGET = "123450"
        NEIGHBORS = [
            [1, 3], [0, 2, 4], [1, 5],
            [0, 4], [1, 3, 5], [2, 4]
        ]

        start = ''.join(map(str, sum(board, [])))

        if start == TARGET:
            return 0

        queue = deque([(start, start.index('0'), 0)])
        visited = {start}

        while queue:
            current_state, zero_index, moves = queue.popleft()

            for neighbor in NEIGHBORS[zero_index]:
                new_state = list(current_state)
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                new_state_str = ''.join(new_state)

                if new_state_str == TARGET:
                    return moves + 1

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, neighbor, moves + 1))

        return -1