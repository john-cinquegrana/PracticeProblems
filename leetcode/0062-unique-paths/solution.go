func uniquePaths(m int, n int) int {
	// Create an m by n matrix of 0s
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}

	// The top left corner is set to 1
	dp[0][0] = 1

	// Set the top-most row and left-most column to 1's, since there's always
	// only one way to get there.
	for i := range dp {
		dp[i][0] = 1
	}

	for i := range dp[0] {
		dp[0][i] = 1
    }

	for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        }
    }

	return dp[m-1][n-1]

}
