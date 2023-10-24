from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        magazine_dict = Counter(magazine)

        for key in rn:
            if key in magazine_dict:
                if rn[key] <= magazine_dict[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True


print(Solution().canConstruct(ransomNote="a", magazine="b"))
print(Solution().canConstruct(ransomNote="aa", magazine="aab"))
print(Solution().canConstruct(ransomNote="bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
