class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        approach 1: greedy
        sort O(n log n)
        use two pointers and select the heaviest with the lightest
        if sum > limit -> choose the heavier 
        else put both together

        approach 2: dp 
        try 


        people = [1,3,2,3,2], limit = 3
        people = [1,2,2,3,3]
        '''

        people.sort() 

        l, r = 0, len(people) - 1
        count = 0
        while l <= r: 
            heavy, light = people[r], people[l]
            if heavy + light > limit: 
                r -= 1
            else: 
                l += 1
                r -= 1
            count += 1
        return count
        