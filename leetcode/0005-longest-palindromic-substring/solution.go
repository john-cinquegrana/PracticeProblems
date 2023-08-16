
func longestPalindrome(s string) string {
	// Create a matrix to hold the values of each palindromic pair
	mat := make([][]bool, len(s))
	// Create the rows in the matrix
	for index := range mat {
		mat[index] = make([]bool, len(s))
	}

	// Create a function that gives true if the two indexes describe a palindrome
	isPalindrome := func (start int, stop int) bool {
		difference := stop - start
		// An empty string is always a palindrome to me
		if (difference <= 0) {
			return true
		} else if difference == 1 {
			return s[start] == s[stop]
		} else if s[start] == s[stop] {
			return mat[start+1][stop-1]
		} else {
			return false
		}
	}

	// Create a variable that will store our best palindrome so far
	longest := ""
	// Iterate over how long of a palindrome we are looking for
	for difference := 0; difference < len(s); difference++ {
		start := 0
		stop := 0 + difference
		for stop < len(s) {
			// Get whether or not this pair is a palindrome
			isPalindrome := isPalindrome(start, stop)
			// Update the matrix with this value
			mat[start][stop] = isPalindrome
            // If the pair is a palindrome
            if isPalindrome {
				// By the nature of this algoirthm, it should be the longest palindrome so far
				longest = s[start:stop+1]
			}
            // Increment the start index
            start++
            // Increment the stop index
            stop++
		}
	}

	return longest
}
