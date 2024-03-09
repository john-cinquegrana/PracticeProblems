class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        key = nums[0]
        for num in nums:
            if num == key:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    key = num
                    count = 1
        return key
