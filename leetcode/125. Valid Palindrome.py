class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = self.del_sign(s)
        s2 = self.del_sign(s)[::-1]

        print(s1)
        print(s2)

        if s1 == s2:
            return True
        else:
            return False

    @staticmethod
    def del_sign(s: str) -> list:
        s_lst = []

        for letter in s:
            if letter.isalpha():
                s_lst.append(letter.lower())
            if letter.isdigit():
                s_lst.append(letter)
            else:
                continue
        return s_lst


print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
