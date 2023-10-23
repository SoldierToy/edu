from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        new_lst = []

        for i in candies:
            if i + extraCandies >= max_candy:
                new_lst.append(True)
            else:
                new_lst.append(False)


        return new_lst
