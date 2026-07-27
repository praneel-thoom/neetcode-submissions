class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        
        while L <= R:
            mid = (L + R) // 2
            if matrix[mid][0] > target:
                R = mid - 1
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                L = mid + 1
            else:
                L1, R1 = 0, len(matrix[mid]) - 1
                while L1 <= R1:
                    mid2 = (L1 + R1) // 2
                    if matrix[mid][mid2] > target:
                        R1 = mid2 - 1
                    elif matrix[mid][mid2] < target:
                        L1 = mid2 + 1
                    else:
                        return True
                return False

        return False