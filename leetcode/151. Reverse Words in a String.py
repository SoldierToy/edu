class Solution:
    def reverseWords(self, s: str) -> str:

        for val in s:
            if val == ' ':
                s.lstrip(' ')
            else:
                break

        for val in s[::-1]:
            if val == ' ':
                s.rstrip(' ')
            else:
                break

        return " ".join([x for x in s.split()[::-1]])


print(Solution().reverseWords("the sky is blue    "))
