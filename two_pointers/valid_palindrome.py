class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())

        for i in range(len(s)):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return False
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(char.lower() for char in s if char.isalnum())

#         for i in range(len(s)//2):
#             if s[i] != s[~i]:
#                 return False
#         return True
