import "fmt"

func climbStairs(n int) int {
  // Create an array that has n entries in it
  ls := make( []int, n+1 )
  // Handle the first two elements exactly
  ls[0] = 1 // index 0
  ls[1] = 1 // index 1
  // Loop over each element in the array to handle the stairs (Treat stairs with 1 indexing)
  for i := 2; i < len(ls); i++ {
      ls[i] = ls[i-1] + ls[i-2]
  }
  // Return the last element in the array, that should have our answer
  return ls[n];
}
