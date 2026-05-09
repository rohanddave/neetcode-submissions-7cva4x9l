class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        when two stones are smashed: contribution = (+y) (-x) / (-y) (+x)
        where the order does not matter 

        so the problem becomes subset selection problem 
        where we want subset sum <= total // 2

        because then we have two subsets and then the answer is 
        the absolute difference between the two 
        subset a sum = X
        subset b sum = total - subset a sum 
        res = min(res, abs(subset a sum - subset b sum))
        '''
        self.res = float('inf')
        self.total = sum(stones)
        memo = {}
        def dfs(i, curr_sum): 
            # base case 
            if i == len(stones): 
                subset_a_sum = curr_sum 
                subset_b_sum = self.total - subset_a_sum 
                return abs(subset_a_sum - subset_b_sum)
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            pick = dfs(i + 1, curr_sum + stones[i])
            skip = dfs(i + 1, curr_sum)
            memo[(i, curr_sum)] = min(pick, skip)
            return memo[(i, curr_sum)]
        return dfs(0, 0)
        