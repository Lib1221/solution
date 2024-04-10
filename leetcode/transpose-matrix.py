class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        another = []
        another = list(list())
        for i in range(len(matrix[0])):
            res = []
            for j in range(len(matrix)):
                res.append(matrix[j][i])
            res = list(res)
            another.append(res)
        return another

                
        
