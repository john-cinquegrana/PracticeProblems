func twoSum(nums []int, target int) []int {
    for i := range nums {
        // If it's a number that can add up, then we try to add
        for j := i+1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }
    // If we found nothing then we return nothing
    return []int{}
}
