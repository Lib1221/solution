class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = ""
        s = ""
        mi = min(len(ele) for ele in strs)
        for i in range(mi):
            s = strs[0][i]
            for j in range(len(strs)):
                if s != strs[j][i]:
                    return str1
            str1 = str1 + s
        return str1
