class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n): 
            res = 0 
            while n: 
                digit = n % 10 
                n = n // 10
                res += digit ** 2 
            return res 
        
        slow, fast = n, n 
        while True: 
            slow = get_next(slow) 
            fast = get_next(get_next(fast))
            if fast == 1:
                return True 
            if slow == fast: 
                return False 
        return True

        