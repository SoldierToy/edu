from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        S = set(nums)

        maxlength = 0

        for e in S:

            if (e - 1) not in S:

                len_n = 1

                while (e + len_n) in S:
                    len_n += 1

                maxlength = max(maxlength, len_n)

        return maxlength
