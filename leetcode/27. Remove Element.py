from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_remove = []

        for i in range(len(nums)):
            if nums[i] == val:
                index_remove.append(i)

        len_ret = len(nums) - len(index_remove)

        index_remove.sort(reverse=True)

        for i in index_remove:
            nums.pop(i)

        return len_ret


# print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
