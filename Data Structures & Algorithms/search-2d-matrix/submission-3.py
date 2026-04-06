class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) - 1
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2
            val = matrix[m_row][-1]
            if val == target:
                return True
            elif val < target:
                l_row = m_row + 1
            else:
                r_row = m_row - 1
        
        if l_row >= len(matrix):
            return False
        
        l_col, r_col = 0, len(matrix[0]) - 1
        while l_col <= r_col:
            m_col = (l_col + r_col) // 2
            curr_val = matrix[l_row][m_col]
            if curr_val == target:
                return True
            elif curr_val < target:
                l_col = m_col + 1
            else:
                r_col = m_col - 1
        return False