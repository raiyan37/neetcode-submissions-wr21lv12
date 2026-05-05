class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while (l < r):
            height = min(heights[l], heights[r])
            base = r - l
            area = base * height
            maxArea = max(area, maxArea)
            
            if (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1

        return maxArea



        