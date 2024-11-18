def twoSum(nums: list[int], target: int):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return [seen[remaining], i]
        seen[value] = i
    return []

inputArr = [3, -3]
solution = twoSum(inputArr, 0)
print(solution)
