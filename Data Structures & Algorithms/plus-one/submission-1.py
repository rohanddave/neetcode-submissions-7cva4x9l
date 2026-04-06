from collections import deque 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = deque() 
        for i in range(len(digits) - 1, -1, -1): 
            digit = digits[i] 
            curr_sum = digit + carry 
            new_digit = curr_sum % 10 
            res.appendleft(new_digit)
            carry = curr_sum // 10 
        if carry: 
            res.appendleft(carry)
        return list(res)
