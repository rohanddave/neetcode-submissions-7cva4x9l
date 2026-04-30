class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(l, r): 
            j = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j], nums[r] = nums[r], nums[j]
            return j
        
        l, r = 0, len(nums) - 1
        target_idx = len(nums) - k
        while True: 
            pivot_idx = helper(l, r)
            if pivot_idx == target_idx:
                return nums[pivot_idx]
            elif pivot_idx < target_idx:
                l = pivot_idx + 1
            else: 
                r = pivot_idx - 1
        
        
        

        