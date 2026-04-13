class Solution:
    def reverseBits(self, n: int) -> int:
        # left and right pointers 
        # if both are the same - do nothing (00, 11)
        # else (01,10) flip both bits 
        res = 0
        for i in range(32):
            digit = n & 1
            n = n >> 1
            res |= (digit << (31 - i))
        return res
        