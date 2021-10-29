class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        memo[0] = 0
        def get_change(num):
            # Base Cases
            if num in memo:
                return memo[num]
            elif num < 0:
                return None
            # Recursively call all subproblems
            min_amount = None
            for coin in coins:
                val = get_change(num-coin)
                if val is not None:
                    if min_amount is None:
                        min_amount = val
                    else:
                        min_amount = min( min_amount, val)
            # The coin we are actually using
            if min_amount is not None:
                min_amount += 1
            # End of logic
            memo[num] = min_amount
            # print( "Value for {} is {}".format(num, min_amount))
            return min_amount
            
        # call the function
        result = get_change(amount)
        if result is None:
            return -1
        else:
            return result
            
                
