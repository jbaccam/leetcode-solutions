class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) 

        top, bottom = 0, ROWS - 1 # top row and bottom row

        while top <= bottom: # similar to l and r binary search but for rows
            row = (top + bottom) // 2 
            if target > matrix[row][-1]: # if our target is greater than the largest value in the current array
                top = row + 1
            elif target < matrix[row][0]: # if our target value is smaller than the smallest value in the current array
                bottom = row - 1
            else: # is in this current row
                break
        
        # This condition is for if the while statement above breaks out, then we never found a row that can contain the value
        if not (top <= bottom): # if the rows passed eachother 
            return False
        
        # we could declare row here just for clarity to know what row we found the value on
        # but in python, variables you assign inside a while or for loop are not scoped to the loop. they stay alive in the         surrounding function
        # so we dont even need to do this since we already calculated what row it was in above
        # row = (top + bottom) // 2 


        l = 0 # first index of the array
        r = COLS - 1 # last index of the array

        # typical binary search
        while l <= r: # iterate until the pointers cross
            mid = (l + r) // 2 # our midpoint
            if target > matrix[row][mid]: # if the target is greater than the value at the midpoint in the row
                l = mid + 1               
            elif target < matrix[row][mid]: # if the target is less than the value at the midpoint in the row
                r = mid - 1
            else:
                return True # must be at the midpoint
        
        # if we never found the value 
        return False