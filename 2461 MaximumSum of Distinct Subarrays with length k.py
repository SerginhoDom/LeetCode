def maximumSubarraySum(nums: list[int], k: int) -> int:
    max_sum = 0
    current_sum = 0
    window = {}

    for i in range(len(nums)):
        current_sum += nums[i]
        window[nums[i]] = window.get(nums[i], 0) + 1

        if i >= k:
            oldest = nums[i - k]
            window[oldest] -= 1
            if window[oldest] == 0:
                del window[oldest]
            current_sum -= oldest

        if i >= k - 1 and len(window) == k:
            max_sum = max(max_sum, current_sum)

    return max_sum if max_sum > 0 else 0

nums = [5,3,3,1,1]
k = 3
print(maximumSubarraySum(nums, k))