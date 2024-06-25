class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)

        # Create the memo for dynamic programming
        answer = [0 for i in range(length)]


        # Start looping over the list backwards
        for i in range(length-2, -1, -1):
            pointer = i + 1
            target = temperatures[i]
            # print(f"Working for temperature {target} at index {i}")
            while pointer < length and temperatures[pointer] < target:
                # We know that we're still in temperatures, and that this
                # temperature is less than or equal to our target.
                if answer[pointer] == 0:
                    pointer += 1
                else:
                    pointer += answer[pointer]
                # print(f"\tpointer is at {pointer}")
            # We are either off the list...
            if pointer >= length:
                answer[i] = 0
            # Or we found a higher temperature
            elif temperatures[pointer] > target:
                answer[i] = pointer - i
            elif temperatures[pointer] == target:
                if answer[pointer] == 0:
                    answer[i] = 0
                else:
                    answer[i] = answer[pointer] + pointer - i
            else:
                raise Exception('Should not be possible')

        return answer

