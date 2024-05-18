class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        s= list(s)
        res = []
        k = 0
        f = 0
        while r < len(s) :
            while l<r and s[r] in res:
                res.pop(f)
                l+=1
            res.append(s[r])
            print(res)
            r+=1
            k = max(r-l, k)
        return k
            
            
