class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def next_greater_scan(nums):
            stack = [] 
            res = [0] * len(nums)
            for i in range(len(nums) - 1, -1, -1):
                while stack and nums[i] >= nums[stack[-1]]:
                    stack.pop()
                
                if stack: 
                    res[i] = stack[-1] - i

                stack.append(i)
            return res
        return next_greater_scan(temperatures)

        