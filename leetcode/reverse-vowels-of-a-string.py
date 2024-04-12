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

        
