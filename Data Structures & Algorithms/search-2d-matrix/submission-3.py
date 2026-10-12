class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colLength = len(matrix[0])
        rowLength = len(matrix)
        l,r = 0, rowLength * colLength - 1
        while l <=r:
            mid = l + (r - l) // 2
            row,col = mid // colLength, mid % colLength
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False