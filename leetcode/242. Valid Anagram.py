from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        if len(s) != len(t):
            return False

        for x in s_dict:
            s_dict_symbol_count = s_dict[x]

            t_dict_symbol_count = t_dict[x]

            if s_dict_symbol_count != t_dict_symbol_count:
                return False

        return True


print(Solution().isAnagram('asd', 'assafd'))
print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
print(Solution().isAnagram("a", "ar"))
print(Solution().isAnagram("aacc", "ccac"))