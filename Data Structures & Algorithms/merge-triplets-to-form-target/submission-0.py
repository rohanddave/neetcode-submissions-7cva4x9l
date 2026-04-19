class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # triplets[j] = [max(ai, bi), max(aj, bj), max(ci, cj)]
        # 1 <= a <= 5; 4 <= b <= 7; 5 <= c <= 6
        # possible values for a = [2, 1, 5]
        # possible values for b = [5, 4, 7]
        # possible values for c = [6, 4, 5]
        '''
        curr = [0, 0, 0]
        to reach a we find a triplet with target_a and a < target_a 
        i = [2, 5, 6]; j = [5, 7, 5]
        merged = [5, 7, 6]
        triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 6]]


        '''

        '''

        '''
        x, y, z = target
        seen = [False, False, False]
        for triplet in triplets: 
            a, b, c = triplet 
            if a > x or b > y or c > z: 
                continue 
            print('valid triplet: ', triplet)
            if a == x:
                seen[0] = True 
            if b == y: 
                seen[1] = True 
            if c == z: 
                seen[2] = True 

        return seen[0] and seen[1] and seen[2]

        