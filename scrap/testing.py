from typing import List
from time import sleep

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # arr.append([0 for i in range(k)])
        # Create the memo to store dp values in
        memo = [0 for i in range(len(arr)+k)]

        for i in range(k, len(arr)+1):
            sum_list = []
            bottom = max(1, i - len(arr) + 1)
            for j in range(bottom, k+1):
                # print(f"i: {i}, j: {j}, sum_list: {sum_list}")
                sum_list.append(
                    memo[i-j] + max(arr[i-j:i])*j
                )
            memo[i] = max(sum_list)
            
        print(memo)
    
sol = Solution()
print(sol.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))
print(sol.maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4))