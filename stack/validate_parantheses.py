class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_bracket_dict = {'}':'{', ')':'(', ']':'['} 

        for char in s:
            if char in close_bracket_dict:
                top = stack.pop() if stack else '#'

                if top != close_bracket_dict[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
