class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        done = [False, False, False]
        for triplet in triplets: 
            a, b, c = triplet 
            if a > x or b > y or c > z: 
                continue 
            if a == x: 
                done[0] = True 
            if b == y: 
                done[1] = True 
            if c == z: 
                done[2] = True 
        return done[0] and done[1] and done[2]

        