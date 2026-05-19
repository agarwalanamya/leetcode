class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m*n - 1

        while left <= right:
            mid = (left + right)//2
            mid_value = matrix[mid // n][mid % n]
            if target == mid_value:
                return True
            elif target < mid_value:
                right = mid - 1
            else:
                left = mid + 1
        
        return False