from collections import Counter


class Solution:
    def findTheDifference(self, st: str, tt: str) -> str:
        cnt1 = Counter(st)
        cnt2 = Counter(tt)

        if len(cnt1) != len(cnt2):
            st = set(st)
            tt = set(tt)
            tt.symmetric_difference_update(st)
            return tt.pop()
        else:
            for k, v in cnt1.items():
                if cnt2[k] != v:
                    return k


print(Solution().findTheDifference('abcd', 'abcde'))
print(Solution().findTheDifference('a', 'aa'))
