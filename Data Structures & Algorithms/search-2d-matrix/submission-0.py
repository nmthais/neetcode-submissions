class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        isNum = False
        rowLength = len(matrix[0])
        targetRow = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][rowLength -1] >= target:
                targetRow = i
        
        for i in range(rowLength):
            if matrix[targetRow][i] == target:
                isNum = True
        return isNum