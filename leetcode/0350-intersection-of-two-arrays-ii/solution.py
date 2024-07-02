class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        # Iterate over the first list, include all these values in a dictionary
        for num in nums1:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        # Iterate over the second list, and add any matching items to the new
        # resulting list
        result = []
        for num in nums2:
            if num in store and store[num] > 0:
                store[num] -= 1
                result.append(num)
        return result
