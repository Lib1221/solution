class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {"(":")","[":"]","{":"}"}
        for i in range(len(s)):
            if s[i] in dict1.keys():
                stack.append(s[i])
            else:
                if [] == stack:
                    return 0
                a = stack.pop()
                if s[i] != dict1[a]:
                    return 0
        return stack == []
