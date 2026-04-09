class Solution:
    def countBits(self, n: int) -> List[int]:
        def get_set_bit_count(n): 
            count = 0 
            while n: 
                count += n & 1
                n >>= 1
            return count 
        res = [] 
        for i in range(n + 1): 
            res.append(get_set_bit_count(i))
        return res

        