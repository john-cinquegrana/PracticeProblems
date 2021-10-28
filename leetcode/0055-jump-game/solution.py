class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i in range(0, len(nums) ):
            if i > max_jump:
                # If we cannot reach this square, we are done
                return False
            elif i + nums[i] > max_jump:
                max_jump = i + nums[i]
        # Every element in the array must be true
        return True
