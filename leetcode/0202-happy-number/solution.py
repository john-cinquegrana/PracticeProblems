class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = []
        def happy_dance(num):
            sum = 0
            og = num
            while(num != 0):
                sum += (num%10) ** 2
                num = num // 10
            # print("Sum from {} is {}".format(og, sum))
            if sum in memo:
                return False
            elif sum == 1:
                return True
            memo.append(sum)
            return happy_dance(sum)
        return happy_dance(n)
