class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []    
        for x in range(len(arr), 1, -1): 
            result.extend([arr.index(x) + 1, x])
            arr = arr[:arr.index(x):-1] + arr[:arr.index(x)]
        return result
