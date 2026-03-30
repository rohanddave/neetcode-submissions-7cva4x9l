class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2 contains unique elements 
        # nums1 is a subset of nums2
        '''
        convert nums1 into set 
        scan nums2 from the right end:
            while stack and nums2[i] >= stack[-1] and current num in nums1 set: 
                stack.pop()
            
            if currentnum in nums1 and stack:
                res.append()
        '''
        stack = [] 
        res = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()
            
            if stack:
                res[nums2[i]] = nums2[stack[-1]]
            stack.append(i)

        return [res.get(n, -1) for n in nums1]

        