class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        l = 1
        while l <= n:
            if l == n:
                return True
            l*=3
        return False
