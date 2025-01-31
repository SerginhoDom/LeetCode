class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}
        for i, value in enumerate(arr):
            remaining1 = value * 2
            if remaining1 in seen:
                return True
            remaining2 = value / 2
            if remaining2 in seen:
                return True
            seen[value] = i
        return False