class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [] 
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr.sort(key=lambda x: x[0])

        stack = []
        for i in range(len(arr) - 1, -1, -1):
            pos, spd = arr[i]
            time = (target - pos) / spd 

            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)



        