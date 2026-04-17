class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = (2 ** 31) - 1, -(2 ** 31)
        res, sign = 0, -1 if x < 0 else 1
        x = abs(x)
        print('x: ', x)
        while x: 
            digit = x % 10 
            if res > (MAX // 10) or (res == (MAX // 10) and digit > (MAX % 10)):
                return 0 
            res = (res * 10) + digit
            print(f'digit: {digit} \t res: {res}')
            x //= 10 

        return sign * res