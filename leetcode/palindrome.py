class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit = 0
        rev = 0
        num = x
        if x < 0:
            return 0
        while x != 0:
            
            digit=x%10
            rev = 10*rev + digit
            x = x//10
        
        if num == rev:
            return 1
        else:
            return 0
