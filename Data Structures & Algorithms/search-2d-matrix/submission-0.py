class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l, r = 0, len(matrix[row]) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if matrix[row][mid] < target:
                    l = mid + 1
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    return True
                
        return False
        
        