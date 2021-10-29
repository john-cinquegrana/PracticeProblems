from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sorted_list = []
        
        for number in nums:
            # If the list is empty, make it not empty
            if not sorted_list: sorted_list.append(number)
            else:
                # Insert the number into the list
                index = bisect_left(sorted_list, number)
                # Check for a duplicate/completeness
                if ((index < len(sorted_list) and sorted_list[index] != number) or index == len(sorted_list)):
                    # If it's a new high we append it
                    if index == len(sorted_list): sorted_list.append(number)
                    # If it's not we do a replacement
                    sorted_list[index] = number
                # print( "Inserted {} into index {} for {}".format(number, index, sorted_list) )
        return len(sorted_list)
                        
