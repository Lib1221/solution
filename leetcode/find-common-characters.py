class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        intsec = set(words[0])
        for i in intsec:
            freq = min(word.count(i) for word in words)
            res += freq*[i]
        return res
        
