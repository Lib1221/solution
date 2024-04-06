class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if len(matrix[0])<2:
                    return 1
                if matrix[i][j] != matrix[i+1][j+1]:
                    return 0
        return 1


        
