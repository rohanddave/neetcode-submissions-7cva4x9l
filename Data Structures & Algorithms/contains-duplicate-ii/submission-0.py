class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        window = set() 
        for r in range(len(nums)):             
            if r > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True  
            window.add(nums[r])
        print(window)
        return False

            

        