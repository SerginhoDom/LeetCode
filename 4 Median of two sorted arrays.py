def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    merged_array = sorted(nums1 + nums2)
    n = len(merged_array)

    if n % 2 == 1:
        return float(merged_array[n // 2])
    else:
        return (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2

arr1 = [1, 3]
arr2 = [2]
print(findMedianSortedArrays(arr1, arr2))

# Оптимальное решение - модификация бинарного поиска