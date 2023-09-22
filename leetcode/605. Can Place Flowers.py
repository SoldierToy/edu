from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0

        flowerbed = [0] + flowerbed + [0]

        for index in range(1, len(flowerbed) - 1):
            element_prev = flowerbed[index - 1]
            element = flowerbed[index]
            element_next = flowerbed[index + 1]

            if element == 0 and element_next == 0 and element_prev == 0:
                counter += 1
                flowerbed[index] = 1

        if counter >= n:
            return True
        else:
            return False


print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
