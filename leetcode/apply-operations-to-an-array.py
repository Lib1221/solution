class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] = nums[i-1]*2
                nums[i] = 0
        t = len(nums)-1
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1
            right +=1
        return nums

        
