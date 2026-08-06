class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) == set(t) and len(s) == len(t):
            for letter in set(s):
                if s.count(letter) != t.count(letter):
                    return False
            return True
        else:
            return False
        