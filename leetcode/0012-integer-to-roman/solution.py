class Solution:
    def intToRoman(self, num: int) -> str:
        # Table to easily define the roman numerals
        rome = {
            'I':	1,
            'V':	5,
            'X':	10,
            'L':	50,
            'C':	100,
            'D':	500,
            'M':	1000,
        }
        rome_list = list(rome.keys())

        # fives = ['V', 'L', 'D']
        # tens = ['I', 'X', 'C', 'M']

        def get_big_digit(num):
            if num >= 10:
                return get_big_digit(num // 10)
            else:
                return num % 10

        result = []

        # Get down to 1000
        while num > 1000:
            result.append('M')
            num -= rome['M']

        while num > 0:
            digit = get_big_digit(num)
            # print(f"Result {result} and num {num}")
            if digit == 4 or digit == 9:
                # Find the next digit that is larger than this number
                big_key = ''
                big_value = 0
                for key, value in rome.items():
                    if value > num:
                        big_key = key
                        big_value = value
                        break
                # Find the item immediately before our key
                big_index = rome_list.index( big_key )
                smaller_index = big_index - (2 if digit == 9 else 1)
                smaller_key = rome_list[smaller_index]
                smaller_value = rome[smaller_key]

                # Change the result and number
                result.append( smaller_key +  big_key)
                value = big_value - smaller_value
                num -= value
            else:
                # Find the biggest numeral that is less than num
                numeral = ''
                val = 0
                for key,value in rome.items():
                    if value > num:
                        break
                    numeral = key
                    val = value
                # Add this to the numeral
                result.append(numeral)
                num -= val

        # print(f"num is {num}")
        # Heyo, we finished the loop
        return "".join(result)
