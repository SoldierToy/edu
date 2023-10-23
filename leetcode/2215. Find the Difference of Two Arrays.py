from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        new_lst = []
        set1 = set(nums1).difference(set(nums2))
        set2 = set(nums2).difference(set(nums1))

        new_lst.append(list(set1))
        new_lst.append(list(set2))

        print(new_lst)

        return new_lst


Solution().findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2])
Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6])
