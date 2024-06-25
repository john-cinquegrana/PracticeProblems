class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # sort the list
        nums.sort()
        # Divide the list into three
        small_size = len(nums) // 3
        # Return the slices
        result = [ [nums[j] for j in range(i*3, (i+1)*3)] for i in range(small_size)  ]
        # Check to make sure it was possible
        for ls in result:
            if ls[-1] - ls[0] > k:
                return []
        # The result was possible
        return result
        
