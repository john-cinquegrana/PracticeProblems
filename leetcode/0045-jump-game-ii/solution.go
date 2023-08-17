
func jump(nums []int) int {
	// Make an array to track the minimum amount of jumps to each space
	jumps := make([]int, len(nums))
	// We start with 1 to make the if-check work, this means we have to subtract 1 on the return
	jumps[0] = 1
	// Iterate over all the *buildings*
	for i := range nums {
		// This is only true if we could make it to this space
		if jumps[i] > 0 {
			// Run for each block we can jump to from here
			for j := i + 1; j < len(nums) && j <= i+nums[i]; j++ {
				// Replace the current value if we can beat it
				if jumps[j]==0 || jumps[i]+1 < jumps[j] {
					jumps[j] = jumps[i] + 1
				}
			}
		}
	}

	// The entire jumps array is now populated. In the problem description, we
	// know we can reach the end, so we just return it immediately.
	return jumps[len(nums)-1] - 1
}

