def maximumSubarraySum(nums: list[int], k: int) -> int:
    sol = 0
    window = nums[:k]

    if len(set(window)) == k:
        sol = sum(window)

    buf = sum(window)

    for i in range(k, len(nums)):
        buf -= window[0]
        window.pop(0)
        window.append(nums[i])
        buf += window[k-1]
        if len(set(window)) == k:
            sol = max(sol, sum(window))

    return sol

nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(maximumSubarraySum(nums, k))