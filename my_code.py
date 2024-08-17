class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        letters = [c for c in s if c.isalpha()]
        

        letters.reverse()
        

        result = []
        

        for char in s:
            if char.isalpha():
                result.append(letters.pop(0))
            else:
                result.append(char)
        
        return ''.join(result)
