class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r= len(nums)-1
        res = 0
        while l < r:
            if nums[r]+nums[l]==k:
                res+=1
                l+=1
                r-=1
            elif nums[r]+nums[l]<k:
                l+=1
            else:
                r-=1
        return res
