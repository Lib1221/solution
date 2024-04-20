class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            area = min(height[left],height[right])*(right-left)
            res = max(area,res)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return res
