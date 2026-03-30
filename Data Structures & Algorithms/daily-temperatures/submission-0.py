class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(0, len(temperatures) - 1): 
            temp = temperatures[i]
            j = i
            while j < len(temperatures) and temperatures[j] <= temp:
                j += 1
            # if j > len(temperatures) and temperatures[len(temperatures)-1] <= temp:
            #     result[i] = 0
            if j < len(temperatures) and temperatures[j] > temp:
                result[i] = j - i


            # if j == len(temperatures) - 1 and temperatures[j] <= temp:
            #     result[i] = 0
            # result[i] = 0 if j >= len(temperatures) and temperatures[j] <= temp else j - i
        return result
        