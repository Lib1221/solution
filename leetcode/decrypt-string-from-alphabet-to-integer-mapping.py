class Solution:
    def freqAlphabets(self, s: str) -> str:
        str1 = ""
        i = len(s)-1
        while i>=0:
            if s[i]=="#":
                str1 = str1 + chr(int(s[i-2:i])+96)
                i=i-2
            else:
                str1 = str1 + chr(int(s[i])+96)
            i -= 1
        return str1[::-1]
        
