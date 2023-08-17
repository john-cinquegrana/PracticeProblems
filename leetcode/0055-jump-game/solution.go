func canJump(nums []int) bool {
	// Create an array to hold whether or not we can reach this index
	canReach := make([]bool, len(nums))
	canReach[0] = true

	// Iterate over the indexes updating numbers based off what we can reach
	for i := range nums {
		if canReach[i] {
			for j := 1; j <= nums[i] && i+j < len(nums); j++ {
				canReach[i+j] = true
			}
		}
	}

	return canReach[len(nums)-1]
}
