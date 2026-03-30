class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l_row, r_row = 0, rows - 1
        l_col, r_col = 0, cols - 1

        while l_row <= r_row: 
            mid_row = (l_row + r_row) // 2
            min_val, max_val = matrix[mid_row][0], matrix[mid_row][cols - 1] 
            if target >= min_val and target <= max_val:
                # binary search in this row
                return self.binarySearch(matrix[mid_row], target)
            elif target > max_val: 
                l_row = mid_row + 1
            else:
                r_row = mid_row - 1
        return False
    def binarySearch(self, arr: List[int], target: int) -> bool:
        l, r = 0, len(arr) -1 
        while l <= r: 
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
