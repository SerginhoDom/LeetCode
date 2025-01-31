def maxSubArray(self, nums: List[int]) -> int:
    local_sum = 0
    global_sum = 0

    if (len(nums) == 0):
        return 0
    
    for i in range(len(nums)):
        if (nums[i] + local_sum < 0):
            local_sum = 0
            continue
        else: 
            local_sum += nums[i]
            if (local_sum > global_sum):
                global_sum = local_sum
    
    if ((len(nums)) > 0) and (global_sum == 0):
        return max(nums)
    
    return global_sum


arr = [0]
print(maxSubArray(arr))