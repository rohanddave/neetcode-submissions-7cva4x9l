from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []  
        for r in range(len(nums)): 
            # maintain the monotonic property
            while window and nums[window[-1]] <= nums[r]: 
                window.pop()
            
            # add the new element
            window.append(r)

            print(r, window)

            if r - k + 1 < 0:
                print('window not full yet so...')
                continue

            # shrink window if left most is supposed to be out of window
            if window[0] <= r - k:
                print(f'shrank window by removing: {window.popleft()}')
            # else:
            #     print('window not full yet so...')
            #     continue
            
            # if there is an answer for the current window
            if window: 
                res.append(nums[window[0]])
            

        return res

            
        