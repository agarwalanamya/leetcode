class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char = {}
        t_char = {}

        for char in s:
             s_char[char] = s_char.get(char, 0) + 1
        for char in t:
             t_char[char] = t_char.get(char, 0) + 1

        if t_char == s_char:
            return True
        return False