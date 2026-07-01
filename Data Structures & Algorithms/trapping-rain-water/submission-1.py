class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        # Two pointers
        l = 0
        r = len(height) - 1

        # Store prefix and suffix maximums
        left_max, right_max = height[l], height[r]
        res = 0

        # Two pointers
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else: 
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        
        return res
