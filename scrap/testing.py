from typing import List
from time import sleep

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ''' We define the median as a value at a specific index i1 in nums1. If
        in nums2 we say this value would have the index i2. If
        i1 + i2 == (m+n)/2 then we know we have the median'''

        # Variables to help us find the median
        low_one = 0
        low_two = 0
        length_one = len(nums1)
        length_two = len(nums2)
        high_one = len(nums1)
        high_two = len(nums2)
        index_sum_goal = (length_one + length_two) // 2

        # The values we're iterating over
        p1 = 0
        p2 = 0

        # small useful functions to increase readability
        def p2_smaller():
            if p1 < 0 or p2 >= length_two:
                return False
            elif p2 < 0 or p1 >= length_one:
                return True
            # Both values are in bounds
            return nums2[p2] < nums1[p1]

        def p1_smaller():
            if p1 < 0 or p2 >= length_two:
                return True
            if p2 < 0 or p1 >= length_one:
                return False
            return nums1[p1] < nums2[p2]

        # Value to hold the result of iteration
        median_index = (-1, -1)

        while median_index == (-1, -1):
            # Iterate the pointer variables
            p1 = (high_one + low_one) // 2
            p2 = (high_two + low_two) // 2
            # current index sum should represent the amount of numbers in the
            # array that are smaller than the minimum of value_one and
            # value_two
            current_index_sum = max(0, p1) + max(0, p2)
            # Compare our current index sum to the goal of our index sum to
            # figure out what to do
            if current_index_sum == index_sum_goal:
                if p1_smaller():
                    # p1 points to the smaller value
                    if p2-1 < 0 or nums2[p2-1] <= nums1[p1]:
                        # We are good and this should be our median.
                        median_index = (p1, p2)
                    else:
                        # p1 is smaller than p2 but also smaller than p2's predecessor
                        # Move p1 up, and move p2 down in the window
                        low_one = p1
                        high_two = p2
                elif p2_smaller():
                    # p2 points to the smaller value
                    if p1-1 < 0 or nums1[p1-1] <= nums2[p2]:
                        # We are good, and p2 should be our median
                        median_index = (p1, p2)
                    else:
                        # p2 is too small and p1 is too big, iterate the search
                        low_two = p2
                        high_one = p1
                else:
                    # Either number could be the median, if either one fulfills
                    # is larger than the counterpart predecessor, we exit the
                    # loop
                    if (p1-1 < 0 or nums1[p1-1] <= nums2[p2]) or (p2-1 < 0 or nums2[p2-1] <= nums1[p1]):
                        median_index = (p1, p2)
                    else:
                        # If they're both equal, and neither fulfills the conditions, idk what to do. This should be impossible,
                        raise Exception('Numbers are equal, but shenanigans')
            elif current_index_sum > index_sum_goal:
                # We need to move down in indices to meet our goal, pick the
                # index that points to the higher value, and knock it down a
                # peg.
                if p1_smaller() and high_two > low_two:
                    high_two = p2
                elif p2_smaller() and high_one > low_one:
                    high_one = p1
                else:
                    # If they're both the same size, it means they're both too
                    # big. We get to hit both of them.
                    high_two = p2
                    high_one = p1
            else:
                # The current sum is less than the goal, we need to move up.
                # Find the index that points to the lower value and move it up.
                if p1_smaller() and low_one < high_one:
                    low_one = p1+1
                elif p2_smaller() and low_two < high_two:
                    low_two = p2+1
                else:
                    # If they're equal, move them both up
                    low_one = p1
                    # In case both numbers are equal, we have to leave this one lower.
                    low_two = p2+1

        # We've exited the loop and the median index should hold the indices
        # that the median is at
        (p1, p2) = median_index
        # print(f"final p1: {p1}, p2: {p2}")

        # If the sum of the lengths is odd, we can just return the median
        if (length_one + length_two) % 2 == 1:
            if p1_smaller():
                return nums1[p1]
            else:
                return nums2[p2]
        # If sum of the lengths is even, we need to average together the two medians
        if (length_one + length_two) % 2 == 0:
            # The smaller element is expected to be the larger median value due
            # to how this algorithm is written. We need to find the next
            # smallest value in either list
            sum = 0
            if p1-1 >= 0 and (p2-1 < 0 or nums1[p1-1] >= nums2[p2-1]):
                # p1 has a larger predecessor, so it comes with
                sum += nums1[p1-1] 
            elif p2-1 >= 0 and (p1-1 < 0 or nums2[p2-1] >= nums1[p1-1]):
                # p2 has a larger predecessor, so it comes with
                sum += nums2[p2-1]
            if p2 < 0 or p2 >= length_two or (p1_smaller() and p1 >= 0 and p1 < length_one):
                sum += nums1[p1]
            else:
                sum += nums2[p2]
            return sum / 2


sol = Solution()
print('2:\t' + str(sol.findMedianSortedArrays([1, 3], [2])))
print('2.5:\t' + str(sol.findMedianSortedArrays([1, 2], [3, 4])))
print('3:\t' + str(sol.findMedianSortedArrays([1, 2, 3, 4, 5], [])))
print('3.5:\t' + str(sol.findMedianSortedArrays([1, 3, 4, 6], [2, 5])))
print('0.0:\t' + str(sol.findMedianSortedArrays([0, 0], [0, 0])))
print('1.0:\t' + str(sol.findMedianSortedArrays([1], [1])))
print('2:\t' + str(sol.findMedianSortedArrays([1, 1, 1, 2, 4, 4, 4], [1, 1, 1, 4, 4, 4])))
print('3.5:\t' + str(sol.findMedianSortedArrays([6], [1, 2, 3, 4, 5])))
print('3.5:\t' + str(sol.findMedianSortedArrays([1, 2, 3, 4, 5], [6])))
print('0.0:\t' + str(sol.findMedianSortedArrays([0,0,0,0,0], [-1,0,0,0,0,0,1])))
print('4.5:\t' + str(sol.findMedianSortedArrays([1, 7, 8], [2, 3, 4, 5, 6])))