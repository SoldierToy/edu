from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        max_val = max(nums_dict.values())
        for k, v in nums_dict.items():
            if v == max_val:
                return k


nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums))
