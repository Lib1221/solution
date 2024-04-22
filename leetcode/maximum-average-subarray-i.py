class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = sum(nums[:k])
        current_maximum = maximum
        for i in range(k,len(nums)):
            maximum = maximum + nums[i] - nums[i-k]
            current_maximum = max(current_maximum, maximum)
        return current_maximum/k
