class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        # Calculate the largest gap between numbers
        last_seen_map = {}
        max_gap_map = {}
        n = len(nums)
        for i in range(2*n):
            index = i % n
            key = nums[index]
            # If we've seen this key before, update the max gap map
            if key in last_seen_map:
                # Mark the largest gap between this element and the last of the
                # same we have seen.
                max_gap_map[key] = max(max_gap_map.get(key, 0), (index - last_seen_map[key] - 1) % n)
            # Mark this as the last place we've seen the element
            last_seen_map[key] = index
        return ceil(min(max_gap_map.values()) / 2)
