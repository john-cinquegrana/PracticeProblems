class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Variables to make it look pretty
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        result = 0

        # Loop over every row in the matrix, and transform it into a cumulative
        # sum of the items before it in the row
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]

        # Now the actual algorithm can start

        # Loop over every combination of columns we can have
        for start in range(num_cols):
            for end in range(start, num_cols):
                # A dictionary of the number of ways we can make a sum with a
                # submatrix bound by the start and end columns.
                lookup = defaultdict(int)
                lookup[0]=1
                # The current sum of our submatrix
                cumsum = 0
                # loop over every row
                for row in range(num_rows):
                    # Add together the submatrix of all the row items in
                    # between the start and end indices
                    if start == 0:
                        cumsum += matrix[row][end]
                    else:
                        cumsum += matrix[row][end] - matrix[row][start-1]
                    # The cumsum represents the value of a current submatrix
                    # that is bound by the start and end columns, and contains
                    # all previous rows. We use the dict to avoid needing a
                    # second loop over the rows. Note that since the cumsum
                    # submatrix and those in lookup have the same width, they
                    # can be subtracted to get a new submatrix of the same
                    # start,end bounds.
                    if cumsum - target in lookup:
                        result += lookup[cumsum - target]
                    # Add our current submatrix to the lookup
                    lookup[cumsum] += 1
        # End of all loops
        return result
