class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get row -> get col
        low, high = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # if last element > target, eliminate rows down
        # if first element < target, eliminate rows above
        while low < high:
            mid = low + (high - low) // 2
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid -1
            else:
                low = mid
                break
        while left <= right:
            m = left + ((right - left) // 2)
            if matrix[low][m] > target:
                right = m - 1
            elif matrix[low][m] < target:
                left = m + 1
            else:
                return True
        return False