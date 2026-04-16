class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0 
        carry = 0 
        for i in range(32): 
            bit_a, bit_b = (a & 1), (b & 1)
            bit = bit_a ^ bit_b ^ carry 
            carry = (bit_a & bit_b) |  (bit_a & carry) | (bit_b & carry)
            res |= (bit << i)
            a, b = (a >> 1), (b >> 1)
        if res >= (1 << 31): 
            res -= (1 << 32)
        return res