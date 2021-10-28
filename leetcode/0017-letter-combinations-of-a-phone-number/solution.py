class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def numtolist(number):
            if number <= 6:
                return list( map( chr, range(number*3 - 6 + 97, number*3 - 6 + 97 + 3) ) )
            elif number == 7:
                return ["p", "q", "r", "s"]
            elif number == 8:
                return ["t", "u", "v"]
            elif number == 9:
                return ["w", "x", "y", "z"]
            else:
                return []
        def prepend_all(pre, ls):
            ''' Prepend the list of characters pre to every string in ls '''
            # print( "Prepending {} to {}".format(pre, ls))
            result = []
            for char in pre:
                result += [ char + word for word in ls]
            if len(ls) == 0: result = pre
            # print("Result is {}".format(result))
            return result
        def dig_to_letters(dig, acc):
            ''' Recursively change list of digits to a list of strings. '''
            # print( "digits left {}. Acc of {}.".format(dig,acc) )
            if len(dig) == 0: return acc
            else:
                return dig_to_letters( dig[:-1], prepend_all( numtolist(int(dig[-1])), acc) )
        return dig_to_letters(digits, [])
            
        
