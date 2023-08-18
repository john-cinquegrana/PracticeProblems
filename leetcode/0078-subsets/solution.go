
func IntPow(base, exp int) int {
    result := 1
    for {
        if exp & 1 == 1 {
            result *= base
        }
        exp >>= 1
        if exp == 0 {
            break
        }
        base *= base
    }
    return result
}

func subsets(nums []int) [][]int {
    // Function to count the bits of an integer
    countBits := func(num int) int {
        count := 0
        // Iterate through the bits of the number to count them up
        for num > 0 {
            count += num & 1
            num = num >> 1
        }
        // Return the count we have calculated
        return count
    }
    // Create the output array that we're gonna be including
    output := make([][]int, IntPow(2, len(nums)))
    // Loop over each index with the output and put the numbers in
    for index := range output {
        // This will be the length of the array
        length := countBits(index)
        // Create the array to actually put in
        arr := make([]int, length)
        placeDex := 0
        // Place the numbers into the array as appropriate
        for i := range nums {
            // If this number matches, then we add it to the set
            if ((1 << i) & index > 0) {
                arr[placeDex] = nums[i]
                placeDex += 1
            }
        }
        // Once the array is complete, we place it in the output
        output[index] = arr
    }
    // Return back the output that we have calculated
    return output
}
