class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p = list(p)
        p.sort()
        k = len(p)
        f = []
        for i in range(0, len(s)-k+1):
            f = s[i:i+k]
            f = list(f)
            f.sort()
            if f == p:
                res.append(i)
        return res
            
