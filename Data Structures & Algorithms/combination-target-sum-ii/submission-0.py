class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        candidates.sort()
        def dfs(i, curr, currSum):
            if currSum == target:
                solutions.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])
            item_popped = curr.pop()
            while i < len(candidates) and candidates[i] == item_popped:
                i+=1
            dfs(i, curr, currSum)
        dfs(0, [], 0)
        return solutions

        