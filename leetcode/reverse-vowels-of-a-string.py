class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a','i','e','o','u']
        index = []
        res = []
        for i in range(len(s)):
            if s[i] in vowels:
                index.append(s[i])
        index.reverse()
        x = 0
        for i in range(len(s)):
            if s[i] in vowels:
                res.append(index[x])
                x+=1
            else:
                res.append(s[i])
        s = ""
        for i in res:
            s+=i
        return s
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            elif s[left] in vowels:
                right-=1
            else:
                left+=1
        return "".join(s)
        """

        
