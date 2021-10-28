class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        print( "Called with k {}".format(k))
        def swap(ls, ind1, ind2):
            temp = ls[ind1]
            ls[ind1] = ls[ind2]
            ls[ind2] = temp
        # Build a dictionary of all the frequencies
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 0
        # Get a unique list of all the keys
        keys = dict.keys()
        # Quickselect to find the k largest frequencies
        min_unsorted = 0
        max_unsorted = len(keys) - 1
        pivot = max_unsorted
        print( "Entering quickselect algo with keys {}".format(keys) )
        # Quickselect Loop, equal elements will be moved below
        while (max_unsorted >= len(keys) - k):
            pivot = max_unsorted
            top = max_unsorted - 1
            store = min_unsorted
            i = min_unsorted
            print("Running quicksort with pivot {} between {} and {}".format(pivot, i, pivot))
            while( i <= top ):
                if dict[keys[i]] < dict[keys[pivot]]:
                    swap(keys, i, store)
                    store += 1
                i += 1
            # Move the pivot to the store
            swap(keys, pivot, store)
            # All items to the left of pivot are <= to pivot
            # Change either max or min unsorted to try and find the specific index
            if store >= len(keys) - k:
                max_unsorted = store - 1
            else: min_unsorted = store + 1
        return keys[-k:]
                
