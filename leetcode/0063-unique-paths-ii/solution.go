
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	// If the first square has an obstacle, return 0 immediately
	if obstacleGrid[0][0] == 1 {
		return 0
	}

	// Create a matrix mat the same dimensions as the obstacle grid
	mat := make([][]int, len(obstacleGrid))
	for i := 0; i < len(mat); i++ {
		mat[i] = make([]int, len(obstacleGrid[0]))
	}

	// Mark the top-left box with a 1
	mat[0][0] = 1

	// Create a helper function that makes it easy to bound around the matrix
	get := func(row, col int) int {
		// If either i or j are out of bounds, return 0
		if row < 0 || col < 0 || row >= len(mat) || col >= len(mat[0]) {
			return 0
		} else {
			// If both i and j are inside bounds, return the respective value
			return mat[row][col]
		}
	}

	// Do the first row a bit special so we can skip it
	for col := 1; col < len(mat[0]); col++ {
		// If there is an obstacle, we put in zeroes
		if obstacleGrid[0][col] == 1 {
			mat[0][col] = 0
		} else {
			// If there's no obstacle, we take the value from the cell before
			mat[0][col] = get(0, col-1)
		}
	}

	// Iterate over every row except the first matrix, counting the number of unique paths, and avoiding obstacles
	for row := 1; row < len(mat); row++ {
		for col := 0; col < len(mat[0]); col++ {
			if obstacleGrid[row][col] == 1 {
				// If the current cell is an obstacle, skip it
				mat[row][col] = 0
			} else {
				// If there are no obstacles, we add up the values from before
				mat[row][col] = get(row-1, col) + get(row, col-1)
			}
		}
	}

	// printMatrix(mat)

	// Return the value of the last cell
	return mat[len(mat)-1][len(mat[0])-1]
}

