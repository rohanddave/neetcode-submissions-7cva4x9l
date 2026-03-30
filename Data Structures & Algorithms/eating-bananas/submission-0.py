import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h hours to finish all bananas 
        # k = bananas per hour 
        # each hour chooses a pile and eats - if pile has less then finishes and does not eat any more 
        '''
        piles = [3,6,7,11], h = 8
        if we pick k = 11 i.e. such that can finish the largest pile i.e. can finish all other piles in 1 hour. therefore k = 4 = length of array

        '''

        # time taken to eat pile = ceil(piles[i]/k)
        # piles = [3,6,7,11], h = 8
        # if k = 4
        # times = [1,2,2,3]
        # speeds = [1,2,3,4,5,6,7,8,9,10,11]

        # piles = [30,11,23,4,20], h = 5
        # if k = 30 
        # times = [1,1,1,1,1]

        # piles = [30,11,23,4,20], h = 6
        # if k = 23 
        # times = [2,1,1,1,1]

        # total number of bananas to eat = 27 in 8 hours 
        # 27/8 = 3.375

        # total = 88; h = 5
        # avg speed = 17.6 = 18
        # times = 

        # if speed = max element then h = length of array 

        # 1. find the max element in the array O(n)
        # 2. create a speeds array from 1...max(piles)
        # 3. binary search over this array by 
        def can_achieve(m): 
            s = 0
            for i in range(len(piles)):
                s += math.ceil(piles[i]/m)
            return s <= h
        l, r = 1, max(piles)
        while l < r: 
            m = (l + r) // 2
            if can_achieve(m):
                r = m
            else: 
                l = m + 1
        return l
