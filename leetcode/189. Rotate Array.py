from typing import List
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new_lst = []

        if len(nums) < k:
            k = k % len(nums)

        for _ in range(k):
            new_lst.append(nums.pop())

        for num in new_lst:
            nums.insert(0, num)


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
Solution().rotate([-1], 2)
Solution().rotate([1, 2], 5)
