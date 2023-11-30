from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        if not digits:
            return []

        if len(digits) == 1:
            return [str(x) for x in num_dict[int(digits)]]

        lst_nums = list(map(int, digits))

        lst_letters = []

        for n in lst_nums:
            lst_letters.append(list(num_dict[n]))

        lst_decart = itertools.product(*lst_letters)

        lst_res = []

        if len(digits) == 2:
            for x, y in lst_decart:
                lst_res.append(x + y)
        elif len(digits) == 3:
            for x, y, i in lst_decart:
                lst_res.append(x + y + i)
        elif len(digits) == 4:
            for x, y, i, z in lst_decart:
                lst_res.append(x + y + i + z)
        return lst_res


print(Solution().letterCombinations('23'))
print(Solution().letterCombinations('234'))
