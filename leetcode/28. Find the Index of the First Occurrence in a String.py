class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ind = haystack.find(needle)
        return ind


print(Solution().strStr(haystack="sadbutsad", needle="skad"))
