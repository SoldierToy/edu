class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string = ''

        all_str = []

        for x in range(len(s)-1):
            string += s[x]
            res = s.split(string)
            for y in res:
                if y == '':
                    all_str.append(True)
                else:
                    all_str.append(False)

            if all(all_str):
                return True

            all_str.clear()

        return False


print(Solution().repeatedSubstringPattern('acacac'))
