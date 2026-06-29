class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)

        # Pointers from each end
        left = 0
        right = n-1
        max_area = 0

        while left < right:
            
            # Update max area if applicable
            curr_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, curr_area)

            # Move the smaller height pointer inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        