from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index_zeros = []

        # проход по nums1 и добавление в index_zeros индексы нулей
        for i in range(len(nums1)):
            if nums1[i] == 0:
                index_zeros.append(i)

            if nums1[i] != 0:
                index_zeros.clear()

        for i in index_zeros:
            if len(nums1) != m:
                nums1.pop()

        nums1.extend(nums2)
        nums1.sort()

        print(nums1)


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
Solution().merge(nums1=[0], m=0, nums2=[1], n=1)
Solution().merge(nums1=[0, 0, 0, 0, 0], m=0, nums2=[1, 2, 3, 4, 5], n=5)
Solution().merge(nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0], m=6, nums2=[1, 2, 2], n=3)
