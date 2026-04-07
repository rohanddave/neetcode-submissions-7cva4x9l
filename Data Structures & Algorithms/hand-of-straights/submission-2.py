class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # we're given a list of hands and a group size 
        # we want to return true if possible to "rearrange"
        # "rearrange" means we want to use all hands to create groups of size groupSize where each group is consecutively increasing by 1
        # example: [1,2,4,2,3,5,3,4] groupSize = 4 => [1,2,3,4], [2,3,4,5]

        n = len(hand)
        if groupSize > n or n % groupSize != 0: 
            return False
        
        '''
        observations: 

        brute force
        1. sort hand in ascending order O(nlogn) => [1,2,2,3,3,4,4,5]
        2. with the first base case we're guaranteed that there will be n / groupSize groups 
        3. for i in range(no_groups):
            group = []
            j = 0 
            while j < n and len(group) < groupSize: 
                if (group and nums[j] == group[-1]) or nums[j] is used:
                    j += 1
                    continue 
                group.append(nums[j])
                mark nums[j] used 
                j += 1
            if len(group) != groupSize: 
                retrun False
        '''

        hand.sort() 
        no_groups = n // groupSize 

        used = [False] * n

        for i in range(no_groups): 
            group = []
            j = 0 
            while j < n and len(group) < groupSize: 
                if (group and hand[j] == group[-1]) or used[j]:
                    j += 1
                    continue 
                
                if group and hand[j] != group[-1] + 1:
                    return False

                group.append(hand[j])
                used[j] = True 
                j += 1
            if len(group) != groupSize: 
                return False
        return True
         