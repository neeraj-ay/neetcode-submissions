class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_vol = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            h_left = heights[left]
            h_right = heights[right]
            h = h_left if h_left < h_right else h_right
            
            volume = (right - left) * h
            if volume > max_vol:
                max_vol = volume

            if h_left < h_right:
                while left < right and heights[left] <= h_left:
                    left += 1
            else:
                while left < right and heights[right] <= h_right:
                    right -= 1
                    
        return max_vol