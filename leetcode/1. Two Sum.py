from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indx1 in range(len(nums)):
            for indx2 in range(len(nums)):
                if (nums[indx1] + nums[indx2] == target) and indx1 != indx2:
                    return [indx1, indx2]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
