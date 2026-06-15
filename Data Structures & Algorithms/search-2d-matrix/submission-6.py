class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        


        l,r = 0, (len(matrix) * len(matrix[0]))-1
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        while l<=r:
            mid = (r-l)//2 + l
            if matrix[mid//num_cols][mid%num_cols] == target:
                return True
            elif matrix[mid//num_cols][mid%num_cols] < target:
                l = mid+1
            else:
                r = mid-1
        return False

            
            
