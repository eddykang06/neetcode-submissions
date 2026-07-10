class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Perform binary search for rows
        l_row = 0 
        r_row = len(matrix) - 1

        while l_row <= r_row:
            m_row = (l_row + r_row) // 2
            if matrix[m_row][-1] < target:
                l_row = m_row + 1
            elif matrix[m_row][-1] > target:
                if matrix[m_row][0] > target:
                    r_row = m_row - 1
                else:
                    break
            else:
                return True

        # Row that might contain the target (correct range)
        row = matrix[m_row]

        l = 0 
        r = len(row) - 1

        # Binary search within potential row 
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m -1
        
        return False

        