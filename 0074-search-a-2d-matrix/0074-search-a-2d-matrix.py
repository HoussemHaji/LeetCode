class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        
        def findRow(top, bottom):
            while top <= bottom: # O(log rows)
                mid = (top + bottom) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][0] < target:
                    top = mid + 1
                else:
                    bottom = mid - 1
            return -1

        row = findRow(top, bottom)
        if row == -1:
            return False

        left = 0
        right = len(matrix[0]) - 1
        while left <= right: # O(log cols)
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False