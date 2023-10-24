class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for letter in s[::-1]:
            if letter.isalpha() :
                cnt += 1

            if cnt > 0 and not letter.isalpha():
                break

        return cnt


print(Solution().lengthOfLastWord('Hello World'))
