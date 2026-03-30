import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
        
        heap = [(-dic[key], key) for key, value in dic.items()]
        kMostFreq = heapq.nsmallest(k, heap)
        result = []
        for item in kMostFreq:
            result.append(item[1])
        return result

        