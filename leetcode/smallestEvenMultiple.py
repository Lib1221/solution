class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        a = n//2
        b = n/2
        if a == b:
            return n
        else:
            return n*2
        
