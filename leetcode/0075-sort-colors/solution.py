class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(ind1, ind2):
            ''' A simple swap function for easy use '''
            temp = nums[ind1]
            nums[ind1] = nums[ind2]
            nums[ind2] = temp
        # Indexes to be iterated over
        mindex = 0
        maxdex = len(nums) - 1
        value_index = 0
        while( value_index <= maxdex ):
            if nums[value_index] == 0:
                # Move to the bottom of the list
                swap(value_index, mindex)
                mindex += 1
                if value_index <= mindex: value_index += 1
            elif nums[value_index] == 2:
                # Move to the top of the list
                swap(value_index, maxdex)
                maxdex -= 1
            elif nums[value_index] == 1:
                value_index += 1
            
