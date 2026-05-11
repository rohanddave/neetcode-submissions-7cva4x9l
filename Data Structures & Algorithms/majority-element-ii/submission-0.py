from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = {} 

        for num in nums: 
            if num in candidates: 
                candidates[num] += 1
            elif len(candidates) < 2: 
                candidates[num] = 1
            else: 
                remove = [] 
                for key in candidates.keys(): 
                    candidates[key] -= 1
                    if candidates[key] == 0:
                        remove.append(key)
                for key in remove: 
                    del candidates[key]
        freq = Counter(nums)

        res = [] 
        for cand in candidates: 
            if freq[cand] > len(nums) // 3:
                res.append(cand)
        return res
        