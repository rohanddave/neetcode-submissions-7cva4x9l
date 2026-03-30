class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = [] 
        candidates.sort() 

        def dfs(start, current, remaining):
            if remaining == 0:
                self.res.append(current[:])
                return 
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                dfs(i + 1, current, remaining - candidates[i])
                current.pop()
        dfs(0, [], target)
        return self.res
        