from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        len_arr = len(arr)
        len_set = len(set(arr))

        if len_arr == len_set:
            return True
        else:
            return False
