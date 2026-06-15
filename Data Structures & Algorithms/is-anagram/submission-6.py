class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht1 = {}
        ht2 = {}
        for char in s:
            ht1[char] = ht1.get(char, 0) + 1
        for char in t:
            ht2[char] = ht2.get(char, 0) + 1
        if ht1 == ht2:
            return True
        return False
        