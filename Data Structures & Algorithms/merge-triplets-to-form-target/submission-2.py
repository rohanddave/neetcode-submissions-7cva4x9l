class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        seen = [False, False, False]
        for triplet in triplets: 
            a, b, c = triplet 
            if a > x or b > y or c > z: 
                continue 
            if a == x:
                seen[0] = True 
            if b == y: 
                seen[1] = True 
            if c == z: 
                seen[2] = True 

        return seen[0] and seen[1] and seen[2]

        