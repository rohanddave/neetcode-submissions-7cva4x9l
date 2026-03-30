class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            num = nums[i]
            remaining = target - num
            if num in dic.keys():
                return [min(i, dic[num]), max(i,dic[num])]
            else:
                dic[remaining] = i
        return []
        