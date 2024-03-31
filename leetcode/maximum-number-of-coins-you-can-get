class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        x = len(piles)//3
        y = 0
        sum = 0
        for i in range(x,len(piles),2):
            sum=sum+piles[i]
        return sum
