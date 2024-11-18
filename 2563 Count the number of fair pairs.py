class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_nums = sorted(nums)
        fair_pairs_count = 0

        # Перебираем каждый элемент, и для каждого ищем диапазон подходящих пар
        for i in range(len(sorted_nums)):
            left_index = i + 1
            right_index = len(sorted_nums) - 1

            # Поиск нижней границы для подходящих значений
            while left_index <= right_index:
                mid = (left_index + right_index) // 2
                if sorted_nums[i] + sorted_nums[mid] < lower:
                    left_index = mid + 1
                else:
                    right_index = mid - 1

            lower_bound = left_index

            # Поиск верхней границы для подходящих значений
            right_index = len(sorted_nums) - 1
            while left_index <= right_index:
                mid = (left_index + right_index) // 2
                if sorted_nums[i] + sorted_nums[mid] > upper:
                    right_index = mid - 1
                else:
                    left_index = mid + 1

            upper_bound = right_index

            # Считаем количество пар, если индексы корректны
            if lower_bound <= upper_bound:
                fair_pairs_count += upper_bound - lower_bound + 1

        return fair_pairs_count