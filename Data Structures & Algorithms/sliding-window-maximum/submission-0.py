class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque([])
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        
        res = [nums[q[0]]]

        for r in range(k, len(nums)):
            if q[0] < r - k + 1:
                q.popleft() 
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            res.append(nums[q[0]])

        return res

        