class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        coords = []
        # Firstly we want to generate all the row's col's to zero out
        # Get the row index of the next 0
        for row in range(0, len(matrix) ):
            while 0 in matrix[row]:
                # Generate all tuples that point to coord of zero
                col = matrix[row].index(0)
                coords.append( (row, col ) )
                matrix[row][col] = -1 # This is fine since we're changing it later anyway
                # We iterate and see if there's another zero in the same line
        for (row, col) in coords:
            # Set the rows to all zeros
            matrix[row] = [0 for i in range(len(matrix[row]))]
            # Set the column to all zeros
            for itrow in range(0, len(matrix)): matrix[itrow][col] = 0
        
        
            
