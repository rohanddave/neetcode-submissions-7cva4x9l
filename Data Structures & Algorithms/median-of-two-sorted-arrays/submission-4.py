class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # a is the shorter list and b is the longer list 
        a, b = nums1, nums2 
        if len(a) > len(b):
            a, b = b, a
        len_a, len_b = len(a), len(b)
        half, total = (len_a + len_b) // 2, len_a + len_b

        l, r = 0, len_a - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            a_left = a[i] if i >= 0 else float('-inf')
            a_right = a[i + 1] if (i + 1) < len_a else float('inf')
            b_left = b[j] if j >= 0 else float('-inf')
            b_right = b[j + 1] if (j + 1) < len_b else float('inf')

            if a_left <= b_right and b_left <= a_right: 
                if total % 2 != 0: 
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right: 
                r = i - 1
            else: 
                l = i + 1
        return -1