class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        k = 0
        for i in range(len(s)):
            if  k < len(spaces) and i == spaces[k]:
                result.append(" ")
                k+=1
            result.append(s[i])
        return "".join(result)
        
