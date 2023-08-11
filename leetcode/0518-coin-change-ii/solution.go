
import "fmt"

func change(amount int, coins []int) int {
    // Create an array to store all of our values
    arr := make([]int, amount+1)
    
    // There is one way to make zero coins
    arr[0] = 1

    // For each in the array, do some work
    for _, coin := range coins {
        // For each index of the array, we try to add up some logic
        for i := coin; i < len(arr); i += 1 {
            // Add the values of the lower index into this one
            arr[i] += arr[i-coin]
        }
    }

    // Now that the array has been set, return the last value
    return arr[amount]
}
