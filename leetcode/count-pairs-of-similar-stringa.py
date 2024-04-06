class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        words.sort()
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                y = set(words[i])
                x = set(words[j])
                if x.issubset(y) and y.issubset(x):
                    count +=1
        return count
        
