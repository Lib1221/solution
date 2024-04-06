class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = int(sqrt(c))
        l = 0
        while l <= d:
            if l * l + d*d ==c:
                return 1
            elif l * l + d*d >=c:
                d -=1
            elif l * l + d*d <=c:
                l+=1
        return 0
        
